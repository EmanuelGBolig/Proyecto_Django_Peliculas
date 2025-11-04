from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from .models import Pelicula


# Create your views here.


class HomePageView(ListView):
    model = Pelicula  # Le decimos que consulte el modelo Pelicula
    template_name = "home.html"  # Sigue usando la misma plantilla
    context_object_name = "peliculas_top"  # Le damos un nombre al contexto

    def get_queryset(self):
        # 2. Esta es la consulta clave:
        # Ordena las películas por puntuación (de mayor a menor)
        # y toma solo las 5 primeras.
        return Pelicula.objects.order_by('-puntuacion')[:5]


class PeliculaListView(ListView):
    model = Pelicula
    template_name = "catalogo.html"
    context_object_name = "peliculas"


class PeliculaDetailView(DetailView):
    model = Pelicula
    template_name = "pelicula_detail.html"
    context_object_name = "pelicula"
