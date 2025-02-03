from django.urls import path
from libros import views
from .views import *

urlpatterns =[
    path("Libros/", views.listaLibros, name="libros"),
    path("Create/", LibroCreateView.as_view(),name= "libro_create"),
    path("Update/<int:pk>/", LibroUpdateView.as_view(), name="libro_update"),
    path("Delete/<int:pk>/", LibroDeleteView.as_view(), name= "libro_delete"),
]