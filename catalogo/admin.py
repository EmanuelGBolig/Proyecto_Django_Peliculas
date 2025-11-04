from django.contrib import admin
from django.db import models
from .models import Pelicula
# 👇 ESTA ES LA LÍNEA CORRECTA PARA LA VERSIÓN 0.3.0 👇
from cloudinary_storage.forms import CloudinaryFileInput 

# Define un Modelo de Admin personalizado
class PeliculaAdmin(admin.ModelAdmin):
    # Esto es lo que fuerza el widget de Cloudinary para el campo 'imagen'
    formfield_overrides = {
        models.ImageField: {'widget': CloudinaryFileInput} 
    }
    
    # (Opcional: esto mejora la vista de lista en el admin)
    list_display = ('titulo', 'autor', 'puntuacion')
    search_fields = ('titulo', 'autor')

# Registra tu modelo USANDO la clase de admin personalizada
admin.site.register(Pelicula, PeliculaAdmin)