from django.db import models


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
    image = models.ImageField(upload_to='products', **NULLABLE)
    category = models.ForeignKey(Category, on_delete = models.PROTECT)
    price = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


    def __str__(self):
        return f'{self.name} ({self.description})'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
