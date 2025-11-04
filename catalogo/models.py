from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    duracion = models.TextField(blank=True, null=True)
    fecha_lanzamiento = models.TextField(blank=True, null=True)
    precuela = models.TextField(blank=True, null=True)
    secuela = models.TextField(blank=True, null=True)
    sinopsis = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='peliculas/', blank=True, null=True)

    puntuacion = models.IntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(5)]
    )

    def __str__(self):
        return self.titulo
