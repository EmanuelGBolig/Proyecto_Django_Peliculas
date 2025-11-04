import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv
import cloudinary  # <-- Importante para el método antiguo

# Definir BASE_DIR primero
BASE_DIR = Path(__file__).resolve().parent.parent

# Carga el archivo .env (solo para desarrollo local)
load_dotenv(BASE_DIR / '.env')

# --- Seguridad ---
SECRET_KEY = os.getenv("SECRET_KEY", "clave-secreta-local-insegura")
DEBUG = os.getenv("DEBUG", "False") == "True"

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
RENDER_EXTERNAL_HOSTNAME = os.getenv("RENDER_EXTERNAL_HOSTNAME")
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
    ALLOWED_HOSTS.append('.onrender.com')


# --- Aplicaciones ---
INSTALLED_APPS = [
    # El orden aquí importa para la v0.3.0
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',  # Para el CSS del admin
    'django.contrib.staticfiles',
    'catalogo',  # Tu app
    'cloudinary_storage',  # La app de storage
    'cloudinary',  # La app principal de cloudinary
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Middleware de Whitenoise
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
        'DIRS': [BASE_DIR / 'templates'],
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
DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600,
    )
}

# --- Validación de Contraseñas (no es necesario cambiar) ---
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'
    },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --- Internacionalización (no es necesario cambiar) ---
LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'America/Argentina/Buenos_Aires'
USE_I18N = True
USE_TZ = True


# --- Configuración de Archivos Estáticos (CSS/JS) ---
# ¡Volvemos al storage estándar de Whitenoise!
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# --- Configuración de Archivos Multimedia (Imágenes subidas) ---
MEDIA_URL = '/media/'
# (No necesitamos MEDIA_ROOT)

# --- Configuración de Cloudinary (MÉTODO ANTIGUO para v0.3.0) ---
# ¡Este es el bloque que faltaba!
cloudinary.config(
    cloud_name=os.getenv('CLOUD_NAME'),
    api_key=os.getenv('API_KEY'),
    api_secret=os.getenv('API_SECRET'),
)

# Esta línea le dice a Django que use Cloudinary para TODAS las subidas
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
# (BORRAMOS CLOUDINARY_STORAGE y STATICFILES_STORAGE de cloudinary)


# --- Configuración por defecto ---
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
