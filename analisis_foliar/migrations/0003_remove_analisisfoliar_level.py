# Generated by Django 5.0.6 on 2024-07-08 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analisis_foliar', '0002_alter_analisisfoliar_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='analisisfoliar',
            name='level',
        ),
    ]
