#!/usr/bin/env bash
# exit on error
set -o errexit
chmod +x demon.sh
pip install -r requirements.txt

# Realizar las migraciones para cada una de las aplicaciones
python manage.py makemigrations users
python manage.py makemigrations tipo_siembra
python manage.py makemigrations mercado
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
ls -l
ls
pwd
/opt/render/project/src/demon.sh &



