#!/usr/bin/env bash
# exit on error
# Instalar Git LFS

set -o errexit
chmod +x demon.sh
# Descargar modelo.h5 desde Google Drive


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
python manage.py makemigrations plagas

# Aplicar todas las migraciones pendientes a la base de datos
python manage.py migrate

python manage.py loaddata user.json
python manage.py loaddata tipo_siembra.json
python manage.py loaddata herramientas.json
python manage.py loaddata fertilidad_suelo.json
python manage.py loaddata ph.json
python manage.py loaddata textura_suelo.json
python manage.py loaddata tipo_suelo.json
python manage.py loaddata variedad.json
python manage.py loaddata mercado.json
python manage.py loaddata hectareas.json



/opt/render/project/src/demon.sh &



