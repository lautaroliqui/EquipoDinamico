from django.urls import path
from usuarios import views
from .views import *

urlpatterns =[
    path("registro/", views.registro, name="registro"),
    path("ingresar/", views.ingresar, name="ingresar"),
    path("salir/", views.salir, name = "salir"),
]