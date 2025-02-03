from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class registrarUsuarioForm(UserCreationForm):
    username = forms.CharField(max_length=20, label='Usuario',
        widget=forms.TextInput(attrs={
            'class': 'form-control loggin',
            'placeholder': 'Nombre de usuario',
        }))
    email = forms.EmailField(label='Email',
        widget=forms.TextInput(attrs={
            'class': 'form-control loggin',
            'placeholder': 'Corre Electrónico',
        }))
    password1 = forms.CharField(label='Contraseña', 
        widget=forms.PasswordInput(attrs={
            'class': 'form-control loggin',
            'placeholder': 'Contraseña',
        }))
    password2 = forms.CharField(label='Repita Contraseña', 
        widget=forms.PasswordInput(attrs={
            'class': 'form-control loggin',
            'placeholder': 'Contraseña',
        }))
    
    class Meta:
        model = User
        fields = ["username","email", "password1","password2"]
        help_text = {k:"" for k in fields}

class ingresarForm(AuthenticationForm):
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