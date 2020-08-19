from django import forms
from .models import *

class AddTasksForm(forms.ModelForm):
    '''Форма для создания новой задачи'''
    class Meta:
        #TODO: Создать нормальную форму с полями и убрать костыль jquery
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
    """ Форма редактирования/закрытие задачи """
    class Meta:
        model = Tasks
        fields = [
            'task',
            'parent',
            'category',
            'finish_date_time',
            'note',
            'close_task'
        ]
        labels = {
            'task': '',
            'parent': '',
            'category': '',
            'finish_date_time': '',
            'note': '',
            'close_task': ''
        }