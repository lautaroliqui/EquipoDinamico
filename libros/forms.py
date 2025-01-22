from django import forms
from .models import *

class LibroForm(forms.ModelForm):
     class Meta:
        model = Libro
        fields = ['id','titulo', 'autor', 'ISBN','numero_Inventario','estado' ,'imagen']


class BusquedaLibroForm(forms.Form):
    query = forms.CharField(label='Buscar libro', max_length=100)


class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['numero_de_pedido', 'nombre', 'apellido', 'libro_solicitado']