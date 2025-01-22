from django.urls import path
from libros import views
from django.conf import settings
from .views import *

urlpatterns =[
    path("base/", views.base, name="base"),
    path("libros/", views.libros, name="libros"),
    path("create/", LibroCreateView.as_view(),name= "libro_create"),
    path("<int:pk>/update/", LibroUpdateView.as_view(), name="libro_update"),
    path("<int:pk>/delete/", LibroDeleteView.as_view(), name= "libro_delete"),
    path("vistaLibros/", ModeloVista, name="vistaLibros"),
    path("busqueda/", views.busqueda, name="busqueda"),
    path("prestamo/", views.PrestamoCreateView.as_view(), name="prestamo"),
    path("vistaPrestamo/", views.vistaPrestamo, name="vistaPrestamo"),
    path("delete/<int:pk>", PrestamoDeleteView.as_view(), name= "prestamo_delete"),
]