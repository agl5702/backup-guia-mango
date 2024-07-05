# Generated by Django 5.0.6 on 2024-07-05 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Informes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_type', models.CharField(max_length=45)),
                ('name', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=45)),
                ('date', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'Informes',
            },
        ),
    ]
