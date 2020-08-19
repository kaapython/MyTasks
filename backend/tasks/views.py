from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from mptt.exceptions import InvalidMove
from mptt.forms import MoveNodeForm

from .models import *
from .forms import *


def index(request, pk=1):
    """" Стартовая страница приложения Tasks """
    hours = []
    for i in range(24):
        hours.append(i)

    minutes = []
    for k in range(0, 60, 5):
        minutes.append(k)
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
    context = {'form': form, 'tasks': tasks, 'cat': cat, 'task': task, 'hours': hours, 'minutes': minutes}
    return render(request, 'tasks/index.html', context)


def alarm_finish_date_time(self):
    """ Функция оповещения срока выполнения задачи """
    now_date_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if now_date_time == self.finish_date_time:
        message = 'Наступила дата задачи {}'.format(self.task)
        return message


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

