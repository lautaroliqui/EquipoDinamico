from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from Apk1 import views
from django.contrib.auth.views import LogoutView



urlpatterns =[
    path("AcercaDe/", views.AcercaDe, name="AcercaDe"),
    path("Inicio/", views.inicio, name="inicio"),
    path("Contacto/", views.contacto, name="contacto"),
]