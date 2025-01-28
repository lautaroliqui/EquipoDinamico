from django import forms
from .models import *


class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['nombre', 'apellido', 'libro_solicitado']
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control custom-input border-0 bg-transparent','placeholder':'Nombre'}),
            'apellido':forms.TextInput(attrs={'class':'form-control custom-input border-0 bg-transparent','placeholder':'Nombre'}),
            'libro_solicitado':forms.TextInput(attrs={'class':'form-control custom-input border-0 bg-transparent','placeholder':'Nombre'}),
        }