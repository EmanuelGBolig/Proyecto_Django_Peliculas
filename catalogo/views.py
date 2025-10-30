from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from .models import Pelicula


# Create your views here.


class HomePageView(TemplateView):
    template_name = "home.html"


class PeliculaListView(ListView):
    model = Pelicula
    template_name = "catalogo.html"
    context_object_name = "peliculas"


class PeliculaDetailView(DetailView):
    model = Pelicula
    template_name = "pelicula_detail.html"
    context_object_name = "pelicula"
