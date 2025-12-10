from django.urls import path
from . import api_views
# urlpatterns = [
#     path('', views.index, name='employees.index'),
#     path('create/', views.create, name='employees.create'),
#     path('edit/<int:id>/', views.edit, name='employees.edit'),
#     path('delete/<int:id>/', views.delete, name='employees.delete'),
# ]

urlpatterns = [
    path('employees/', api_views.employee_list_create),
    path('employees/<int:id>/', api_views.employee_detail),
]