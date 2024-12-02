#!/usr/bin/env bash
# exit on error
# Instalar Git LFS

set -o errexit
chmod +x demon.sh
# Descargar modelo.h5 desde Google Drive
echo "Descargando modelo.h5 desde Google Drive..."
MODEL_URL="https://drive.google.com/uc?id=1XwYZ12345abcDEFG6789HI"
curl -L -o plagas/modelo.h5 "$MODEL_URL"
echo "Modelo descargado exitosamente."

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

/opt/render/project/src/demon.sh &



