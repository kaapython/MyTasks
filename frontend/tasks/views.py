from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from mptt.exceptions import InvalidMove
from mptt.forms import MoveNodeForm

from .models import *
from .forms import *
from backend.services import _get_hours, _get_minutes


def index(request, pk=1):
    """" Стартовая страница приложения Tasks """
    tasks = Tasks.objects.all().exclude(close_task=True).order_by('id')
    task = Tasks.objects.get(id=pk)
    cat = Tasks.objects.filter(category_id=pk)
    if request.method != 'POST':
        form = AddTasksForm
    else:
        form = AddTasksForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.save())
            return HttpResponseRedirect(reverse('index'))
    context = {'form': form, 'tasks': tasks, 'cat': cat, 'task': task,
               'hours': _get_hours(), 'minutes': _get_minutes()}
    return render(request, 'tasks/index.html', context)


def edit_task(request, pk):
    """ Редактирование/закрытие задачи """
    task = Tasks.objects.get(id=pk)
    if request.method != 'POST':
        form = EditTaskForm(instance=task)
    else:
        form = EditTaskForm(instance=task, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index', args=[task.id]))
    context = {'task': task, 'form': form}
    return render(request, 'tasks/edit_task.html', context)
