from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from .models import Pelicula
from django.db.models import Q


# Create your views here.


class HomePageView(ListView):
    model = Pelicula
    template_name = "home.html"
    # Cambiamos el nombre del contexto para que sea más claro
    context_object_name = "peliculas_lista_plana"

    def get_queryset(self):
        # Obtenemos las 6 películas con mejor puntuación
        # (Usamos 6 para tener 2 slides completos)
        return Pelicula.objects.order_by('-puntuacion')[:6]

    def get_context_data(self, **kwargs):
        # Obtenemos el contexto base
        context = super().get_context_data(**kwargs)

        # Obtenemos la lista plana de películas
        lista_plana = context['peliculas_lista_plana']

        # --- Esta es la lógica para agrupar en trozos de 3 ---
        chunk_size = 3
        lista_agrupada = [
            lista_plana[i : i + chunk_size]
            for i in range(0, len(lista_plana), chunk_size)
        ]

        # Añadimos la nueva lista agrupada al contexto
        context['peliculas_agrupadas'] = lista_agrupada

        return context


class PeliculaListView(ListView):
    model = Pelicula
    template_name = "catalogo.html"
    context_object_name = "peliculas"

    def get_queryset(self):
        query = self.request.GET.get('q')

        if query:
            object_list = self.model.objects.filter(
                Q(titulo__icontains=query) | Q(autor__icontains=query)
            )
        else:
            object_list = self.model.objects.all()

        return object_list


class PeliculaDetailView(DetailView):
    model = Pelicula
    template_name = "pelicula_detail.html"
    context_object_name = "pelicula"
