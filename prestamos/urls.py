from django.urls import path
from prestamos import views
from .views import *

urlpatterns = [
    path("prestamos/", views.Prestamos, name='prestamos'),
    path("crearPrestamo/", views.PrestamoCreateView.as_view(), name='prestamo_create'),
    path("update/<int:pk>", PrestamoUpdateView.as_view(), name='prestamo_update'),
    path("delete/<int:pk>", PrestamoDeleteView.as_view(), name= 'prestamo_delete'),
]