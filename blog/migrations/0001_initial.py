# Generated by Django 5.0.3 on 2024-04-10 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Заголовок')),
                ('slug', models.CharField(max_length=250, verbose_name='Слаг')),
                ('description', models.TextField(verbose_name='Содержание')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='posts', verbose_name='Изображение')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('count_view', models.SmallIntegerField(default=0, verbose_name='Количество просмотров')),
                ('author', models.CharField(max_length=250, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'запись',
                'verbose_name_plural': 'записи',
            },
        ),
    ]
