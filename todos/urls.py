from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('toggle/<int:pk>/', views.todo_toggle, name='todo_toggle'),
    path('edit/<int:pk>/', views.todo_edit, name='todo_edit'),
    path('delete/<int:pk>/', views.todo_delete, name='todo_delete'),
    path('clear-completed/', views.todo_clear_completed, name='todo_clear_completed'),
]
