from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

from mptt.exceptions import InvalidMove
from mptt.forms import MoveNodeForm

from .models import *
from .forms import *
from backend.services import _get_hours, _get_minutes


def index(request, pk=1):
    """" Стартовая страница приложения Tasks """
    tasks = Tasks.objects.all().exclude(close_task=True).order_by('id')
    try:
        task = Tasks.objects.get(id=pk)
    except ObjectDoesNotExist:
        form = AddTasksForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        return render(request, 'tasks/add_task.html', {'form': form})
    cat = Tasks.objects.filter(category_id=pk)
    if request.method != 'POST':
        form = AddTasksForm
    else:
        form = AddTasksForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    context = {'form': form, 'tasks': tasks, 'cat': cat, 'task': task,
               'hours': _get_hours(), 'minutes': _get_minutes()}
    return render(request, 'tasks/index.html', context)


def add_task(request):
    form = AddTasksForm(request.POST)
    if form.is_valid():
        form.save()
        print(form.save())
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
        return JsonResponse({'message': f'Категория {query_category} добавлена'})
