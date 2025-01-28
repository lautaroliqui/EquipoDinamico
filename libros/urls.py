from django.urls import path
from libros import views
from .views import *

urlpatterns =[
    path("libros/", views.listaLibros, name="libros"),
    path("create/", LibroCreateView.as_view(),name= "libro_create"),
    path("<int:pk>/update/", LibroUpdateView.as_view(), name="libro_update"),
    path("<int:pk>/delete/", LibroDeleteView.as_view(), name= "libro_delete"),
    path("vistaLibros/", Busqueda, name="vistaLibros"),
]