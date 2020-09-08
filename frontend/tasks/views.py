from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from time import strftime

from mptt.exceptions import InvalidMove
from mptt.forms import MoveNodeForm

from .models import *
from .forms import *
from backend.services import _get_hours, _get_minutes


def index(request, pk=1):
    """" Стартовая страница приложения Tasks """
    tasks = Tasks.objects.all().exclude(close_task=True).order_by('id')
    all_category = Category.objects.all()
    priority = Priority.objects.all()
    try:
        task = Tasks.objects.get(id=pk)
    except ObjectDoesNotExist:
        form = AddTasksForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        return render(request, 'tasks/add_task.html', {'form': form})
    if request.is_ajax():
        pk_category = request.GET.get('pk_category')
        pk_priority = request.GET.get('pk_priority')
        print('pk_importance', pk_priority)
        cat = Tasks.objects.filter(category_id=pk_category,
                                   priority_id=pk_priority).exclude(
            close_task=True).order_by('id')
        items = {}
        for i in range(len(cat)):
            items[i] = {
                'color': cat[i].priority.color,
                'pk': cat[i].pk,
                'task': cat[i].task,
                'parent': ['нет' if cat[i].parent is None
                           else cat[i].parent.task],
                'create_date_time': cat[i].create_date_time.strftime("%d.%m.%Y"),
                'note': cat[i].note,
                'finish_date_time': ['' if cat[i].finish_date_time is None
                                     else cat[i].finish_date_time]
            }
        items = items
        return JsonResponse(items)
    if request.method != 'POST':
        form = AddTasksForm
    else:
        form = AddTasksForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    context = {'form': form, 'tasks': tasks, 'task': task,
               'hours': _get_hours(), 'minutes': _get_minutes(),
               'all_category': all_category, 'priority': priority}
    return render(request, 'tasks/index.html', context)


def add_task(request):
    """ Добавление новой задачи """
    form = AddTasksForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('index'))
    context = {'form': form}
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


def add_category(request):
    """ Добавление новой категории """
    if request.is_ajax():
        query_category = request.GET.get('category')
        category = Category()
        category.name = query_category
        category.save()
        return JsonResponse(
            {'message': f'Категория {query_category} добавлена'})
