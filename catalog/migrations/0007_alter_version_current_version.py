# Generated by Django 5.0.3 on 2024-04-26 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='current_version',
            field=models.BooleanField(default=False, verbose_name='признак текущей версии'),
        ),
    ]
