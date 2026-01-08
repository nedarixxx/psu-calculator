from django.contrib import admin
from .models import Category, Component, Build


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'component_count']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'description']
    ordering = ['name']
    
    def component_count(self, obj):
        return obj.components.count()
    component_count.short_description = 'Компонентов'


@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'power_draw', 'price', 'form_factor', 'created_at']
    list_filter = ['category', 'created_at']
    search_fields = ['name', 'description', 'form_factor']
    ordering = ['category', 'name']
    readonly_fields = ['created_at']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'category', 'form_factor', 'description')
        }),
        ('Технические характеристики', {
            'fields': ('power_draw', 'price')
        }),
        ('История', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )


@admin.register(Build)
class BuildAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'component_count', 'total_power', 'created_at']
    list_filter = ['user', 'created_at', 'updated_at']
    search_fields = ['title', 'description', 'user__username']
    readonly_fields = ['created_at', 'updated_at', 'display_components']
    filter_horizontal = ['components']
    ordering = ['-created_at']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'user', 'description')
        }),
        ('Компоненты', {
            'fields': ('components', 'display_components')
        }),
        ('История', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def component_count(self, obj):
        return obj.components.count()
    component_count.short_description = 'Компонентов'
    
    def total_power(self, obj):
        return f"{obj.get_total_power()} Вт"
    total_power.short_description = 'Всего потребление'
    
    def display_components(self, obj):
        components = obj.components.all()
        if not components:
            return 'Компонентов нет'
        
        html = '<ul>'
        for comp in components:
            html += f'<li>{comp.name} ({comp.power_draw}W) - {comp.category.name}</li>'
        html += '</ul>'
        return html
    display_components.short_description = 'Выбранные компоненты'
    
    def get_readonly_fields(self, request, obj=None):
        readonly = list(self.readonly_fields)
        if obj:  # Редактирование существующей сборки
            readonly.append('display_components')
        return readonly
