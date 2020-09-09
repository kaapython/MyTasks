from django.contrib import admin
from django.urls import path

from .views import *
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>', views.index, name='index'),
    path('add_category', views.add_category, name='add_category'),
    path('edit_task/<int:pk>', views.edit_task, name='edit_task'),
]
