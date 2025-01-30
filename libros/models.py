from django.db import models

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=30)
    autor = models.CharField(max_length=20)
    ISBN = models.CharField(max_length=13)
    numero_Inventario = models.IntegerField()
    estado = models.CharField(max_length=10)
    imagen = models.ImageField(upload_to="libros")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.titulo