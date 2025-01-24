from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from Apk1 import views
from django.contrib.auth.views import LogoutView



urlpatterns =[
    path("base/", views.base, name="base"),
    path("AcercaDe/", views.AcercaDe, name="AcercaDe"),
    path("inicio/", views.inicio, name="inicio"),
    path("contacto/", views.contacto, name="contacto"),
]