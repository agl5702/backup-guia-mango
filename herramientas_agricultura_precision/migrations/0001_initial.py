# Generated by Django 5.0.6 on 2024-07-05 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoMercado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, verbose_name='Nombre del tipo de mercado')),
                ('description', models.TextField(max_length=1000, verbose_name='Descripción del tipo de mercado')),
            ],
            options={
                'verbose_name_plural': 'Tipos de mercados',
            },
        ),
        migrations.CreateModel(
            name='Herramientas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=145, verbose_name='Nombre de la herramienta')),
                ('description', models.TextField(max_length=500, verbose_name='Descripción de la herramienta')),
                ('type_market', models.ManyToManyField(to='herramientas_agricultura_precision.tipomercado')),
            ],
            options={
                'verbose_name_plural': 'Herramientas',
            },
        ),
    ]
