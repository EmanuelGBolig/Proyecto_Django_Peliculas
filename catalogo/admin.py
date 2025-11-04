from django.contrib import admin
from django.db import models
from .models import Pelicula  # <-- Cambia 'Pelicula' por el nombre de tu modelo si es diferente
from cloudinary.forms import CloudinaryFileField

# Define un Modelo de Admin personalizado
class PeliculaAdmin(admin.ModelAdmin):
    # Esto es lo que fuerza el widget de Cloudinary para el campo 'imagen'
    formfield_overrides = {
        models.ImageField: {'widget': CloudinaryFileField}
    }
    
    # (Opcional: esto mejora la vista de lista en el admin)
    list_display = ('titulo', 'autor', 'puntuacion')
    search_fields = ('titulo', 'autor')

# Registra tu modelo USANDO la clase de admin personalizada
admin.site.register(Pelicula, PeliculaAdmin) 

# Si tenías una línea simple como 'admin.site.register(Pelicula)', bórrala.