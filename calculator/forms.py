from django import forms
from .models import Build, Component, Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class BuildForm(forms.ModelForm):
    """Форма для создания/редактирования сборки"""
    
    class Meta:
        model = Build
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Например: Игровой ПК 2025',
                'required': True
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Дополнительные заметки о вашей сборке...',
                'rows': 3
            })
        }


class AddComponentToBuildForm(forms.Form):
    """Форма для добавления компонента в сборку с поиском и фильтрацией"""
    
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'category_select'
        }),
        label='Категория',
        empty_label='-- Все категории --'
    )
    
    search = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'search_input',
            'placeholder': 'Поиск по названию...'
        }),
        label='Поиск'
    )
    
    component = forms.ModelChoiceField(
        queryset=Component.objects.select_related('category'),
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'component_select'
        }),
        label='Выберите компонент',
        empty_label='-- Выберите компонент --'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # По умолчанию показываем все компоненты
        self.fields['component'].queryset = Component.objects.select_related(
            'category'
        ).order_by('category__name', 'name')


class ComponentFilterForm(forms.Form):
    """Форма для фильтрации компонентов по категориям"""
    category = forms.ModelChoiceField(
        queryset=None,
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-control'
        }),
        empty_label='-- Все категории --'
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from .models import Category
        self.fields['category'].queryset = Category.objects.all()


class CustomUserCreationForm(UserCreationForm):
    """Форма регистрации с дополнительными полями"""
    email = forms.EmailField(
        required=True,
        help_text='Укажите вашу электронную почту'
    )
    first_name = forms.CharField(
        max_length=30,
        required=False,
        help_text='Имя (необязательно)'
    )
    last_name = forms.CharField(
        max_length=150,
        required=False,
        help_text='Фамилия (необязательно)'
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Добавляем CSS классы для Bootstrap
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        
        # Убираем справку о пароле (слишком длинная)
        self.fields['password1'].help_text = 'Минимум 8 символов, не только цифры'
        self.fields['password2'].help_text = 'Повторите пароль'

    def clean_email(self):
        """Проверяем, что email уникален"""
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с таким email уже зарегистрирован')
        return email

    def save(self, commit=True):
        """Сохраняем пользователя с email"""
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user