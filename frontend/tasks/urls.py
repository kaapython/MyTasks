from django.contrib import admin
from django.urls import path

from .views import *
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>', views.index, name='index'),
    # path('task', views.task, name='task'),
    # path('task/<int:pk>', views.task, name='task'),
    path('edit_task/<int:pk>', views.edit_task, name='edit_task'),
    # path('task/close_task', views.close_task, name='close_task'),
    # path('close_task', views.close_task, name='close_task'),
]
