from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('catalogo/', views.PeliculaListView.as_view(), name='catalogo'),
    path('movie/<int:pk>/', views.PeliculaDetailView.as_view(), name='pelicula_detail'),
]
