# Generated by Django 3.2.18 on 2023-04-24 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags_ingr', '0003_auto_20230423_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
