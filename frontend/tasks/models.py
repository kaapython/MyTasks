from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
import datetime


class Category(models.Model):
    """ Категории задач """
    name = models.CharField('Категория', max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


class Importance(models.Model):
    """ Определение важности задач """
    importance = models.IntegerField(default=0, null=True, blank=True,
                                     help_text='Важность задачи')


class Tasks(MPTTModel):
    """ Иерархическая структура задач """
    task = models.CharField('Задача', max_length=50, unique=True,
                            help_text='Задача', db_index=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True,
                            blank=True, related_name='children',
                            verbose_name='Родитель', help_text='Родитель')
    slug = models.SlugField('slug', max_length=50)
    create_date_time = models.DateTimeField('Дата создания', auto_now_add=True,
                                            blank=True)
    category = models.ForeignKey(Category, verbose_name='Категории',
                                 on_delete=models.CASCADE,
                                 help_text='Категория')

    finish_date_time = models.DateTimeField('Дата оповещения', default='',
                                            blank=True, null=True,
                                            help_text='Дата оповещения')
    note = models.CharField('Заметка', default='', blank=True, max_length=500,
                            help_text='Заметка')
    close_task = models.BooleanField('Выполнено', default=False, blank=True)

    def __str__(self):
        return self.task

    class MPTTMeta:
        order_insertion_by = ['id']
