from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Category(models.Model):
    """Категория компонентов (CPU, GPU, RAM и т.д.)"""
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Название категории"
    )
    slug = models.SlugField(
        unique=True,
        verbose_name="URL-идентификатор"
    )
    description = models.TextField(
        blank=True,
        default="",
        verbose_name="Описание"
    )
    icon = models.CharField(
        max_length=50,
        default="fa-microchip",
        help_text="Bootstrap icon class (например: fa-microchip)"
    )

    class Meta:
        ordering = ['name']
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Component(models.Model):
    """Компонент ПК (процессор, видеокарта, память и т.д.)"""
    name = models.CharField(
        max_length=200,
        verbose_name="Название компонента"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='components',
        verbose_name="Категория"
    )
    power_draw = models.IntegerField(
        validators=[MinValueValidator(1)],
        verbose_name="Энергопотребление (Вт)",
        help_text="TDP или типичное потребление в Ваттах"
    )
    # Пиковое потребление (для видеокарт особенно важно)
    peak_power = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)],
        verbose_name="Пиковое потребление (Вт)",
        help_text="Максимальное потребление при пиковых нагрузках"
    )
    # Рекомендованная мощность БП от производителя
    recommended_psu = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)],
        verbose_name="Рекомендованная мощность БП (Вт)",
        help_text="Рекомендованная мощность блока питания для этого компонента"
    )
    
    psu_wattage = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)],
        verbose_name="Мощность БП (Вт)",
        help_text="Номинальная мощность для блоков питания (берёт power_draw если не указано)"
    )
    
    price = models.IntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(0)],
        verbose_name="Средняя цена (₽)"
    )
    form_factor = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Форм-фактор (напр. AM5, LGA1700, ITX, ATX)"
    )
    description = models.TextField(
        blank=True,
        default="",
        verbose_name="Характеристики"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата добавления"
    )

    class Meta:
        ordering = ['category', 'name']
        verbose_name = "Компонент"
        verbose_name_plural = "Компоненты"
        indexes = [
            models.Index(fields=['category']),
        ]

    def __str__(self):
        return f"{self.name} ({self.power_draw}W)"


class Build(models.Model):
    """Пользовательская конфигурация ПК"""
    title = models.CharField(
        max_length=200,
        verbose_name="Название сборки"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='builds',
        verbose_name="Пользователь"
    )
    components = models.ManyToManyField(
        Component,
        related_name='builds',
        verbose_name="Компоненты",
        blank=True
    )
    description = models.TextField(
        blank=True,
        default="",
        verbose_name="Описание/примечания"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления"
    )

    class Meta:
        ordering = ['-updated_at']
        verbose_name = "Сборка"
        verbose_name_plural = "Сборки"
        indexes = [
            models.Index(fields=['user']),
        ]

    def __str__(self):
        return f"{self.title} ({self.user.username})"

    def get_total_power(self):
        """Получить суммарное потребление всех компонентов"""
        return self.components.aggregate(
            total=models.Sum('power_draw')
        )['total'] or 0

    def get_recommended_psu(self):
        """Рекомендованная мощность БП (надежный расчет)"""
        components = self.components.all()
        
        if not components.exists():
            return 0
        
        # Суммируем типичное потребление
        total_power = self.get_total_power()
        
        # Применяем коэффициент безопасности 1.3x
        recommended = int(total_power * 1.3)
        
        # Также проверяем максимальное рекомендованное значение от производителей
        max_recommended = 0
        for component in components:
            if component.recommended_psu > 0 and component.recommended_psu > max_recommended:
                max_recommended = component.recommended_psu
        
        # Берем максимум из двух расчетов
        return max(recommended, max_recommended)
    
    def get_psu_recommendations(self):
        """
        - Возвращает детальные рекомендации по БП
        - Для видеокарты (если есть) - от производителя
        - Для всей сборки - на основе пикового потребления всех компонентов
        """
        components = self.components.all()
        
        if not components.exists():
            return {
                'gpu_psu': 0,
                'build_psu': 0,
                'gpu_name': 'Видеокарта не добавлена'
            }
        
        # ========== РЕКОМЕНДАЦИЯ ДЛЯ ВИДЕОКАРТЫ ==========
        gpu_component = None
        gpu_psu = 0
        
        gpu_category = Category.objects.filter(slug='gpu').first()
        if gpu_category:
            gpu_component = components.filter(category=gpu_category).first()
            if gpu_component and gpu_component.recommended_psu > 0:
                gpu_psu = gpu_component.recommended_psu
        
        # ========== РЕКОМЕНДАЦИЯ ДЛЯ ВСЕЙ СБОРКИ ==========
        # Суммируем пиковое потребление ВСЕх компонентов
        total_peak_power = 0
        for component in components:
            peak = component.peak_power if component.peak_power > 0 else component.power_draw
            total_peak_power += peak
        
        # Применяем коэффициент безопасности 1.25x к пиковому потреблению
        build_psu = int(total_peak_power * 1.25)
        
        return {
            'gpu_psu': gpu_psu,
            'gpu_name': gpu_component.name if gpu_component else 'Видеокарта не добавлена',
            'build_psu': build_psu,
            'total_peak_power': total_peak_power
        }

    def get_recommended_psus(self):
        """
        Возвращает список рекомендуемых блоков питания
        на основе расчетной мощности (±50W)
        
        Ищет БП по полю power_draw (мощность БП)
        """
        # Получаем рекомендуемую мощность БП
        build_psu = self.get_psu_recommendations()['build_psu']
        
        if build_psu == 0:
            return []
        
        # Ищем блоки питания в диапазоне ±50W
        min_power = build_psu - 50
        max_power = build_psu + 50
        
        # Получаем категорию PSU
        psu_category = Category.objects.filter(slug='psu').first()
        
        if not psu_category:
            return []
        
        # Находим подходящие блоки питания по их мощности (power_draw)
        recommended_psus = Component.objects.filter(
            category=psu_category,
            power_draw__gte=min_power,
            power_draw__lte=max_power
        ).order_by('power_draw')
        
        return recommended_psus


    def get_components_by_category(self):
        """Получить компоненты сгруппированные по категориям"""
        components = self.components.all()
        grouped = {}
        for component in components:
            cat_name = component.category.name
            if cat_name not in grouped:
                grouped[cat_name] = []
            grouped[cat_name].append(component)
        return grouped
