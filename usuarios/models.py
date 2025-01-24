from django.db import models
from django import forms
from django.contrib.auth.forms import AuthenticationForm

# Create your models here.
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label='Usuario',
        widget=forms.TextInput(attrs={
            'class': 'form-control loggin',
            'placeholder': 'Nombre de usuario',
        })
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control loggin',
            'placeholder': 'Contraseña',
        })
    )