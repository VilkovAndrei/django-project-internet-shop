from django.db import models
from django.shortcuts import reverse

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class OurContact(models.Model):
    title = models.CharField(max_length=150, verbose_name='наименование')
    country = models.CharField(max_length=100, verbose_name='страна')
    inn = models.CharField(max_length=12, verbose_name='ИНН')
    address = models.CharField(max_length=250, verbose_name='адрес')
    phone = models.CharField(max_length=50, verbose_name='телефон')
    email = models.EmailField()

    def __str__(self):
        return f'{self.title}'

    def get_absolut_url(self):
        return reverse('catalog:contacts', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'наш контакт'
        verbose_name_plural = 'наши контакты'


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
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='категория')
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='время редактирования')
    parent = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='создатель', **NULLABLE)
    is_published = models.BooleanField(default=False, verbose_name='признак публикации')

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        permissions = [
            (
                "set_published_status",
                "Can set published status"
            ),
            (
                "change_description",
                "Can change description"
            ),
            (
                "change_category",
                "Can change category"
            )
        ]

    def __str__(self):
        return f'{self.name} ({self.description})'

    def get_absolut_url(self):
        return reverse('catalog:product_detail', kwargs={'pk': self.pk})


class Version(models.Model):

    product = models.ForeignKey(Product, verbose_name='продукт', on_delete=models.CASCADE, related_name='versions')
    number = models.CharField(max_length=50, verbose_name='номер версии')
    name = models.CharField(max_length=150, verbose_name='название версии')
    current_version = models.BooleanField(default=False, verbose_name='признак текущей версии')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
