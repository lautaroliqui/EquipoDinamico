from django.urls import path
from usuarios import views
from .views import *

urlpatterns =[
    path("Registro/", views.registro, name="registro"),
    path("Ingresar/", views.ingresar, name="ingresar"),
    path("Salir/", views.salir, name = "salir"),
]