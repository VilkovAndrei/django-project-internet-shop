from django.db import models
from datetime import datetime


NULLABLE = {'blank':True, 'null':True}

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.CharField(max_length=250, verbose_name='описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.CharField(max_length=200, verbose_name='описание')
    image = models.ImageField(upload_to='products', verbose_name='фото', **NULLABLE)
    category = models.ForeignKey(Category, on_delete = models.PROTECT, verbose_name='категория')
    price = models.IntegerField()
    created_at = models.DateTimeField(default=datetime.now, verbose_name='время создания')
    updated_at = models.DateTimeField(verbose_name='время редактирования')


    def __str__(self):
        return f'{self.name} ({self.description})'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
