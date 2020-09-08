from django import forms
from .models import *


class AddTasksForm(forms.ModelForm):
    """ Форма для создания новой задачи """

    class Meta:
        model = Tasks
        fields = [
            'task',
            'parent',
            'category',
            'finish_date_time',
            'note'
        ]
        labels = {
            'task': '',
            'parent': '',
            'category': '',
            'finish_date_time': '',
            'note': ''
        }


class EditTaskForm(forms.ModelForm):
    """ Форма редактирования/закрытия задачи """

    class Meta:
        model = Tasks
        fields = [
            'priority',
            'task',
            'parent',
            'category',
            'finish_date_time',
            'note',
            'close_task'
        ]
        labels = {
            'priority': '',
            'task': '',
            'parent': '',
            'category': '',
            'finish_date_time': '',
            'note': '',
            'close_task': ''
        }
