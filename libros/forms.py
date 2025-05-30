from django import forms
from .models import *

class LibroForm(forms.ModelForm):
    ESTADO_CHOICES =[
        ('', 'Selecciona...'),
        ('nuevo', 'Nuevo'),
        ('como_nuevo', 'Como Nuevo'),
        ('bueno', 'Bueno'),
        ('aceptable', 'Aceptable'),
        ('usado', 'Usado'),
        ('dañado', 'Dañado')
        ]
    estado = forms.ChoiceField(choices=ESTADO_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'ISBN', 'numero_Inventario', 'estado', 'imagen']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control custom-input border-0',
                'placeholder': 'Título del libro'
            }),
            'autor': forms.TextInput(attrs={
                'class': ' border-0 bg-transparent',
            }),
            'ISBN': forms.TextInput(attrs={
                'class': 'form-control custom-input',
                'placeholder': 'ISBN'
            }),
            'numero_Inventario': forms.NumberInput(attrs={'class': 'form-control custom-input', 'placeholder': 'Número de Inventario'}),
            'imagen': forms.FileInput(attrs={
                'class': 'form-control form-control-sm','type':'file','id': 'formFileSm'
            })
        }

    def clean_numero_Inventario(self):
        numero_Inventario = self.cleaned_data.get('numero_Inventario')
        if numero_Inventario < 0:
            raise forms.ValidationError('El número de inventario no puede ser negativo.')
        return numero_Inventario


class BusquedaLibroForm(forms.Form):
    query = forms.CharField(label='Buscar libro', max_length=100)