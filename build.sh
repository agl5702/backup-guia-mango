#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# Realizar las migraciones para cada una de las aplicaciones
python manage.py makemigrations users
python manage.py makemigrations tipo_siembra
python manage.py makemigrations herramientas_agricultura_precision
python manage.py makemigrations hectareas
python manage.py makemigrations suelo
python manage.py makemigrations analisis_suelo
python manage.py makemigrations variedad_mango
python manage.py makemigrations cultivo
python manage.py makemigrations analisis_foliar
python manage.py makemigrations informes
python manage.py makemigrations tablas_estadisticas

# Aplicar todas las migraciones pendientes a la base de datos
python manage.py migrate

# Crear un superusuario (si es necesario)
#python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin@admin.com', 'admin', 'admin')"
