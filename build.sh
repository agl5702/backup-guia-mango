#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt
python makemigrations users
python makemigrations tipo_siembra
python makemigrations herramientas_agricultura_precision
python makemigrations hectareas
python makemigrations suelo
python makemigrations variedad_mango
python makemigrations cultivo
python makemigrations analisis_foliar
python makemigrations informes
python makemigrations tablas_estadisticas
python manage.py migrate
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin@admin.com', 'admin', 'admin')"