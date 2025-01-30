from django.db import models

# Create your models here.
class Prestamo(models.Model):
    numero_de_pedido = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    libro_solicitado = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)