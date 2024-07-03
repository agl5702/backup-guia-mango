# Generated by Django 5.0.6 on 2024-07-03 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hectareas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('description', models.TextField(max_length=100, verbose_name='Descripción')),
                ('number_trees', models.IntegerField(default=0, verbose_name='Cantidad de Árboles')),
            ],
        ),
    ]
