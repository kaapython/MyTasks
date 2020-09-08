from typing import Tuple
from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """ Категории """
    list_display = ("name", "id")
    list_display_links: Tuple[str] = ('name',)


@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    """ Задачи """
    list_display = (
        "priority",
        "task",
        "parent",
        "slug",
        "id"
    )
    list_display_links: Tuple[str] = ('task',)
    list_filter = ('task',)
    prepopulated_fields = {"slug": ("task",)}


@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    """ Важность задачи """
    list_display = ("priority", "color", "id")
    list_display_links: Tuple[str] = ('priority',)
