from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class UsuarioNuevo(UserCreationForm):
    username = forms.CharField(max_length=50)
    email = forms.EmailField()
    password1 = forms.CharField(label = "Ingrese contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repita su contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username","email", "password1","password2"]
        help_text = {k:"" for k in fields}


