from django.db import models
from django.shortcuts import reverse
from pytils.translit import slugify

NULLABLE = {'blank': True, 'null': True}


class Post(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    slug = models.CharField(max_length=250, unique=True, verbose_name='Слаг')
    description = models.TextField(verbose_name='Содержание')
    preview = models.ImageField(upload_to='posts', verbose_name='Изображение', **NULLABLE)
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    count_view = models.SmallIntegerField(default=0, verbose_name='Количество просмотров')
    author = models.CharField(max_length=250, verbose_name='Автор')

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        """
        Сохранение полей модели при их отсутствии заполнения
        """
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'записи'
