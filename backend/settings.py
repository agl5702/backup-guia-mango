

from datetime import timedelta
import os
from pathlib import Path

import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: don't run with debug turned on in production!
SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key_here')

# Configuración para activar o desactivar la depuración según el entorno
DEBUG = os.environ.get('RENDER') != 'true'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# TOKEN_EXPIRED_AFTER_SECONDS=60
ALLOWED_HOSTS = ['*']
CORS_ALLOW_ALL_ORIGINS = True

MODEL_PATH = os.path.join(BASE_DIR, 'plagas', 'modelo.h5')


RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)



# Application definition

INSTALLED_APPS = [
    # Base Apps
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Local Apps
    'cultivo',
    'hectareas',
    'mercado',
    'herramientas_agricultura_precision',
    'informes',
    'analisis_suelo',
    'suelo',
    'tablas_estadisticas',
    'tipo_siembra',
    'users',
    'variedad_mango',
    'analisis_foliar',
    'plagas',


    # Third Apps
    'corsheaders',
    'rest_framework',
    'drf_yasg',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'static/templates/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600
    )
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
if not DEBUG:

    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework_simplejwt.authentication.JWTAuthentication',
        ),
    'DEFAULT_PERMISSION_CLASSES':(
        'rest_framework.permissions.AllowAny',
    )

}

AUTH_USER_MODEL= 'users.User'

SIMPLE_JWT={
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=120),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    'ROTATE_REFRESH_TOKENS':True,
    'BLACKLIST_AFTER_ROTATION': True
}

SWAGGER_SETTINGS = {
    'DOC_EXPANSION': 'none',
}

JAZZMIN_SETTINGS = {
    'site_title': 'Keitt Web',
    # Name sidebar admin app
    'site_brand': 'Keitt Web',
    'site_header': 'Mango',
    'site_footer': 'SENA',
    'site_logo': 'images/logo.png',
    'login_logo':'images/keittweb.png',
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        
        "users.User":"fas fa-users",

        "analisis_foliar.AnalisisFoliar": "fas fa-leaf",

        "analisis_suelo.AnalisisSuelo": "bi bi-clipboard-data-fill",

        "cultivo": "fas fa-tractor",
        "cultivo.Cultivo": "fas fa-tractor",

        "suelo.TexturaSuelo": "fas fa-layer-group",
        "suelo.pH":"fas fa-vial",
        "suelo.TipoSuelo":"fas fa-mountain",
        "suelo.DrenajeSuelo": "fas fa-tint",

        "suelo.FertilidadSuelo": "icon-mango",

        "informes.Informes":"fas fa-file-alt", 
        
        "mercado.TipoMercado":"fas fa-cart-arrow-down",
        "hectareas.Hectareas":"icon-hectarea",
        "tipo_siembra.TipoSiembra":"icon-tsiembra",
        "tablas_estadisticas.TablasEstadisticas":"fas fa-chart-bar",
        "herramientas_agricultura_precision.Herramientas":"fas fa-tools",
        "variedad_mango.VariedadMango":"icon-vmango",
        "plagas.Plaga":"fas fa-bug",
    },


    }