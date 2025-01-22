from django.db import models
from django.db import models

from django.contrib.auth.models import User


class Libro(models.Model):
    id = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=30)
    autor = models.CharField(max_length=15)
    ISBN = models.CharField(max_length=13)
    numero_Inventario = models.IntegerField()
    estado = models.CharField(max_length=10)
    imagen = models.ImageField(upload_to="libros")
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.titulo


class Prestamo(models.Model):

    numero_de_pedido = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=20)
    libro_solicitado = models.CharField(max_length=60)


