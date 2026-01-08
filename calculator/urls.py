from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'calculator'

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    
    # Компоненты
    path('components/', views.component_list, name='component_list'),
    
    # Сборки
    path('builds/', views.build_list, name='build_list'),
    path('builds/create/', views.build_create, name='build_create'),
    path('builds/<int:pk>/', views.build_detail, name='build_detail'),
    path('builds/<int:pk>/edit/', views.build_edit, name='build_edit'),
    path('builds/<int:pk>/delete/', views.build_delete, name='build_delete'),
    
    # AJAX операции
    path('builds/<int:build_id>/components/<int:component_id>/remove/', 
         views.remove_component, name='remove_component'),
    
    path('register/', views.register, name='register'),
    
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='calculator:index'), name='logout'),
]
