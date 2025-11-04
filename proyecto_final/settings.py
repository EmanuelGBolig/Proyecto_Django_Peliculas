import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv  # Para leer el .env




# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Carga el archivo .env (solo para desarrollo local)
load_dotenv(BASE_DIR / '.env')

# --- Seguridad ---
# Lee la SECRET_KEY desde el entorno (Render o .env)
SECRET_KEY = os.getenv("SECRET_KEY", "clave-secreta-local-insegura")

# DEBUG estará en 'True' solo si la variable DEBUG es 'True'
DEBUG = os.getenv("DEBUG", "False") == "True"

# Hosts permitidos
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# Añade el host de Render automáticamente si existe
RENDER_EXTERNAL_HOSTNAME = os.getenv("RENDER_EXTERNAL_HOSTNAME")
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
    ALLOWED_HOSTS.append('.onrender.com') # Añade el wildcard por si acaso


# --- Aplicaciones ---
# El orden es importante para Cloudinary y el Admin
INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',  # Para que Whitenoise sirva CSS en local
    'cloudinary_storage',             # Debe ir ANTES del admin
    'cloudinary',                     # Debe ir ANTES del admin
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Tu app
    'catalogo',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Middleware de Whitenoise
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'proyecto_final.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Carpeta global de templates
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

WSGI_APPLICATION = 'proyecto_final.wsgi.application'


# --- Base de Datos ---
# Usa PostgreSQL en Render (leyendo DATABASE_URL)
# Usa db.sqlite3 en local
DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600,
    )
}


# --- Validación de Contraseñas ---
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# --- Internacionalización ---
LANGUAGE_CODE = 'es-es' # Español
TIME_ZONE = 'America/Argentina/Buenos_Aires' # Tu zona horaria
USE_I18N = True
USE_TZ = True


# --- Configuración de Archivos Estáticos (CSS/JS) ---
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles' # Carpeta para 'collectstatic' en Render
STATICFILES_STORAGE = 'cloudinary_storage.storage.CloudinaryWhiteNoiseStaticFilesStorage'


# --- Configuración de Archivos Multimedia (Imágenes subidas) ---
MEDIA_URL = '/media/' 
# (No necesitamos MEDIA_ROOT, Cloudinary lo maneja)

# Esta es la configuración MODERNA que lee las variables de entorno
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv('CLOUD_NAME'),
    'API_KEY': os.getenv('API_KEY'),
    'API_SECRET': os.getenv('API_SECRET'),
}

# Esta línea le dice a Django que use Cloudinary para TODAS las subidas
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


# --- Configuración por defecto ---
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'