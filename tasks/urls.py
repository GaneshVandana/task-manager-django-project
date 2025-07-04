from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add/', views.add_task, name='add_task'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
    path('update/<int:pk>/', views.update_task, name='update_task'),  #  Update task
    path('signup/', views.signup_view, name='signup'),               #  Signup
]
