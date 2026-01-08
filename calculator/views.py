from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.db.models import Sum, Count
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from io import BytesIO
import base64
import json
from .models import Build, Component, Category
from .forms import BuildForm, AddComponentToBuildForm, ComponentFilterForm
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm
from django.core.paginator import Paginator

# Используем Agg backend для matplotlib (без GUI)
matplotlib.use('Agg')

def generate_pie_chart(build):
    """
    Генерирует круговую диаграмму распределения энергопотребления по категориям.
    Возвращает base64-encoded PNG изображение.
    """
    components = build.components.all()
    if not components.exists():
        return None

    # Создание DataFrame для анализа
    data = []
    for component in components:
        data.append({
            'category': component.category.name,
            'power': component.power_draw
        })
    df = pd.DataFrame(data)
    power_by_category = df.groupby('category')['power'].sum()

    # Создание графика
    fig, ax = plt.subplots(figsize=(8, 6), facecolor='white')
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#F7DC6F']
    wedges, texts, autotexts = ax.pie(
        power_by_category.values,
        labels=power_by_category.index,
        autopct='%1.1f%%',
        startangle=90,
        colors=colors[:len(power_by_category)]
    )

    # Улучшение стиля текста
    for text in texts:
        text.set_fontsize(11)
        text.set_weight('bold')
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(10)
        autotext.set_weight('bold')
    ax.set_title('Распределение энергопотребления по категориям', fontsize=14, weight='bold', pad=20)

    # Сохранение в буфер памяти
    buffer = BytesIO()
    plt.savefig(buffer, format='png', bbox_inches='tight', dpi=100)
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode()
    plt.close(fig)

    return image_base64

def get_analytics_data(build):
    """
    ✅ ИСПРАВЛЕНО: Возвращает аналитические данные о сборке
    - Суммарное потребление (типичное)
    - Пиковое потребление (СУММИРОВАНИЕ всех компонентов!)
    - Рекомендации по БП
    - Разбивка по категориям
    """
    components = build.components.all()

    # Типичное потребление (сумма всех)
    total_power = build.get_total_power()

    # ✅ ИСПРАВЛЕНО: Пиковое потребление - суммируем для всех компонентов
    total_peak_power = 0
    for component in components:
        peak = component.peak_power if component.peak_power > 0 else component.power_draw
        total_peak_power += peak

    # Рекомендации по БП
    psu_recommendations = build.get_psu_recommendations()

    # Разбивка по категориям
    categories_power = []
    for category in Category.objects.all():
        power = components.filter(category=category).aggregate(
            total=Sum('power_draw')
        )['total'] or 0

        if power > 0:
            categories_power.append({
                'category': category.name,
                'power': power,
                'percentage': round((power / total_power * 100), 1) if total_power > 0 else 0
            })

    return {
        'total_power': total_power,
        'peak_power': total_peak_power,  # ✅ Теперь это сумма всех пиковых!
        'gpu_psu': psu_recommendations['gpu_psu'],
        'gpu_name': psu_recommendations['gpu_name'],
        'build_psu': psu_recommendations['build_psu'],  # ✅ Рассчитано на основе пикового потребления
        'categories_power': categories_power,
        'component_count': components.count()
    }

@login_required
def build_list(request):
    """Отображение списка всех сборок текущего пользователя"""
    builds = Build.objects.filter(user=request.user).prefetch_related('components')

    # Статистика
    total_builds = builds.count()
    total_components = sum(b.components.count() for b in builds)

    context = {
        'builds': builds,
        'total_builds': total_builds,
        'total_components': total_components,
    }

    return render(request, 'calculator/build_list.html', context)

@login_required
def build_create(request):
    """Создание новой сборки"""
    if request.method == 'POST':
        form = BuildForm(request.POST)
        if form.is_valid():
            build = form.save(commit=False)
            build.user = request.user
            build.save()
            messages.success(request, f'Сборка "{build.title}" создана успешно!')
            return redirect('calculator:build_detail', pk=build.pk)
    else:
        form = BuildForm()

    return render(request, 'calculator/build_form.html', {'form': form, 'title': 'Создать новую сборку'})

@login_required
def build_detail(request, pk):
    """Отображение деталей сборки с аналитикой"""
    build = get_object_or_404(Build, pk=pk, user=request.user)
    components = build.components.all().select_related('category')

    # Получение аналитических данных
    analytics = get_analytics_data(build)

    # ✅ НОВОЕ: Получаем рекомендуемые блоки питания
    recommended_psus = build.get_recommended_psus()

    # Генерация графика
    chart_image = generate_pie_chart(build)

    # Форма для добавления компонента
    if request.method == 'POST':
        if 'add_component' in request.POST:
            form = AddComponentToBuildForm(request.POST)
            if form.is_valid():
                component = form.cleaned_data['component']
                # Проверка, чтобы не добавить один компонент дважды
                if not build.components.filter(pk=component.pk).exists():
                    build.components.add(component)
                    messages.success(request, f'{component.name} добавлен в сборку')
                else:
                    messages.warning(request, 'Этот компонент уже в сборке')
                return redirect('calculator:build_detail', pk=build.pk)
        form = AddComponentToBuildForm()
    else:
        form = AddComponentToBuildForm()

    context = {
        'build': build,
        'components': components,
        'analytics': analytics,
        'recommended_psus': recommended_psus,  # ✅ НОВОЕ
        'chart_image': chart_image,
        'form': form,
    }

    return render(request, 'calculator/build_detail.html', context)

@login_required
def build_edit(request, pk):
    """Редактирование сборки"""
    build = get_object_or_404(Build, pk=pk, user=request.user)

    if request.method == 'POST':
        form = BuildForm(request.POST, instance=build)
        if form.is_valid():
            form.save()
            messages.success(request, 'Сборка обновлена')
            return redirect('calculator:build_detail', pk=build.pk)
    else:
        form = BuildForm(instance=build)

    return render(request, 'calculator/build_form.html', {
        'form': form,
        'build': build,
        'title': f'Редактировать "{build.title}"'
    })

@login_required
def build_delete(request, pk):
    """Удаление сборки"""
    build = get_object_or_404(Build, pk=pk, user=request.user)

    if request.method == 'POST':
        build_title = build.title
        build.delete()
        messages.success(request, f'Сборка "{build_title}" удалена')
        return redirect('calculator:build_list')

    return render(request, 'calculator/build_confirm_delete.html', {'build': build})

@login_required
@require_http_methods(["POST"])
def remove_component(request, build_id, component_id):
    """AJAX: Удаление компонента из сборки"""
    build = get_object_or_404(Build, pk=build_id, user=request.user)
    component = get_object_or_404(Component, pk=component_id)
    build.components.remove(component)

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # Вернуть обновленные аналитические данные
        analytics = get_analytics_data(build)
        return JsonResponse({
            'status': 'success',
            'message': f'{component.name} удален',
            'analytics': analytics
        })

    messages.success(request, f'{component.name} удален из сборки')
    return redirect('calculator:build_detail', pk=build.pk)

# @login_required
def component_list(request):
    """Отображение каталога компонентов (доступно всем)"""
    form = ComponentFilterForm(request.GET or None)
    components = Component.objects.select_related('category')

    # Фильтрация по категориям
    if form.is_valid() and form.cleaned_data.get('category'):
        components = components.filter(category=form.cleaned_data['category'])

    # Группировка по категориям
    categories = Category.objects.all()
    components_by_category = {}
    page_number = request.GET.get('page', 1)

    for category in categories:
        cat_components = components.filter(category=category)
        if cat_components.exists():
            paginator = Paginator(cat_components, 20)
            paginated = paginator.get_page(page_number)
            components_by_category[category] = paginated

    context = {
        'form': form,
        'components_by_category': components_by_category,
        'total_components': Component.objects.count(),
    }

    return render(request, 'calculator/component_list.html', context)

def index(request):
    """Главная страница"""
    # Статистика
    total_builds = Build.objects.count()
    total_components = Component.objects.count()
    total_users = Build.objects.values('user').distinct().count()

    # Топ 5 самых мощных компонентов
    top_components = Component.objects.order_by('-power_draw')[:5]

    context = {
        'total_builds': total_builds,
        'total_components': total_components,
        'total_users': total_users,
        'top_components': top_components,
    }

    return render(request, 'calculator/index.html', context)

def register(request):
    """Страница регистрации новых пользователей"""
    if request.user.is_authenticated:
        # Если уже авторизован - перенаправляем на главную
        return redirect('calculator:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Создаём пользователя
            user = form.save()

            # Автоматически авторизуем после регистрации
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

            messages.success(request, f'Добро пожаловать, {username}! Вы успешно зарегистрировались.')
            return redirect('calculator:index')
        else:
            # Выводим ошибки
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})
