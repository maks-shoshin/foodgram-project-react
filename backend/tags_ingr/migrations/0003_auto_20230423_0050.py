# Generated by Django 3.0 on 2023-04-22 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags_ingr', '0002_auto_20230423_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='measurement_unit',
            field=models.CharField(max_length=200, verbose_name='Единица измерения'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
    ]
