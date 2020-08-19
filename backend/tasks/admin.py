from typing import Tuple
from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Категории"""
    list_display = ("name", "id")
    list_display_links: Tuple[str] = ('name',)


@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    """ Задачи """
    list_display = ("task", "parent", "id")
    list_display_links: Tuple[str] = ('task',)
    list_filter = ('task',)
    prepopulated_fields = {"slug": ("task",)}


@admin.register(Importance)
class ImportanceAdmin(admin.ModelAdmin):
    """Важность задачи"""
    list_display = ("importance", "id")
    list_display_links: Tuple[str] = ('importance',)