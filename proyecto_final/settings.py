"""
Django settings for proyecto_final project.
"""

from pathlib import Path
import os
import dj_database_url

# --- Rutas base ---
BASE_DIR = Path(__file__).resolve().parent.parent

# --- Seguridad ---
SECRET_KEY = os.environ.get('SECRET_KEY')

# DEBUG solo se activa si la variable de entorno DEBUG=True
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# --- Hosts permitidos ---
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Render asigna un hostname de entorno
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Como respaldo, acepta cualquier subdominio de onrender.com
ALLOWED_HOSTS.append('.onrender.com')


# --- Aplicaciones instaladas ---
INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',  # antes de las de django
    'cloudinary_storage',  # para almacenamiento de archivos estáticos/media
    'cloudinary',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'catalogo',  # tu app
]


# --- Middleware ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # debe ir aquí, justo después de SecurityMiddleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# --- URLs / WSGI ---
ROOT_URLCONF = 'proyecto_final.urls'
WSGI_APPLICATION = 'proyecto_final.wsgi.application'


# --- Templates ---
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# --- Base de datos ---
DATABASES = {}

if 'DATABASE_URL' in os.environ:
    # Base de datos en Render (PostgreSQL)
    DATABASES['default'] = dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600,
        ssl_require=True,
    )
else:
    # Base de datos local
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }


# --- Validadores de contraseña ---
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'
    },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# --- Internacionalización ---
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# --- Archivos estáticos (CSS/JS) ---
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Whitenoise: sirve archivos comprimidos y versionados
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# --- Archivos multimedia (subidos por el usuario) ---
MEDIA_URL = '/media/'

# Usa Cloudinary como backend de almacenamiento para las subidas
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Configuración de Cloudinary
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUD_NAME'),
    'API_KEY': os.environ.get('API_KEY'),
    'API_SECRET': os.environ.get('API_SECRET'),
}


# --- Seguridad adicional para producción ---
# Render usa HTTPS, por lo tanto configuramos CSRF
CSRF_TRUSTED_ORIGINS = [
    'https://' + os.environ.get('RENDER_EXTERNAL_HOSTNAME', ''),
    'https://proyecto-peliculas-el7d.onrender.com',
]

# Seguridad recomendada
SECURE_SSL_REDIRECT = not DEBUG
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG


# --- Archivos estáticos adicionales (opcional) ---
# Django buscará también dentro de estas rutas
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]


# --- Config por defecto de Django ---
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
