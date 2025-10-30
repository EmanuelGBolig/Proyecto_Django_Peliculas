from django.contrib import admin
from .models import Pelicula  # 1. Importa tu modelo 'Libro'

# 2. Registra el modelo en el sitio de administración
admin.site.register(Pelicula)
