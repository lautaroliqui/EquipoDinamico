from django.urls import path
from prestamos import views
from .views import *

urlpatterns = [
    path("Prestamos/", views.Prestamos, name='prestamos'),
    path("CrearPrestamo/", views.PrestamoCreateView.as_view(), name='prestamo_create'),
    path("Update/<int:pk>", PrestamoUpdateView.as_view(), name='prestamo_update'),
    path("Delete/<int:pk>", PrestamoDeleteView.as_view(), name= 'prestamo_delete'),
]