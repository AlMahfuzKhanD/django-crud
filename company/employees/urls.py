from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='employees.index'),
    path('create/', views.create, name='employees.create'),
    path('edit/<int:id>/', views.edit, name='employees.edit'),
    path('delete/<int:id>/', views.delete, name='employees.delete'),
]