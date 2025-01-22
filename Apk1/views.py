from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import UsuarioNuevo
from django.contrib.auth import logout

from django.contrib.auth.models import User


# Create your views here.

def base(request):
    return render(request,"Apk1/base.html")

def inicio(request):
    return render(request,"Apk1/inicio.html")

def AcercaDe(request):
    return render(request,"Apk1/AcercaDe.html")

def contacto(request):
    return render(request,"Apk1/contacto.html")

def registro(request):
    if request.method == "POST":
        form = UsuarioNuevo(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            form.save()
            return render(request, "Apk1/registro.html", {"mensaje": (f"El usuario {username} creado correctamente")})
        else:
            return render(request, "Apk1/registro.html", {"form": form, "mensaje": "Error al crear el usuario"})
    else:
        form= UsuarioNuevo()
    return render(request, "Apk1/registro.html", {"form": form})


def ingresar(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usu = form.cleaned_data.get("username")
            clave = form.cleaned_data.get("password")
            usuario1 = authenticate(username = usu, password = clave)#trae un usuario de la base
            if usuario1 is not None:
                login(request, usuario1)
                return render(request, "Apk1/ingresar.html",{"mensajeCorrecto": (f"BIENVENIDO! : {usuario1}")})
            else:
                return render(request,"Apk1/ingresar.html", {"mensajeIncorrecto": "Usuario o contraseña incorrectos"})#Diosito sabe
        else:
            return render(request, "Apk1/ingresar.html",{"mensajeIncorrecto": "Usuario o contraseña incorrectos"})
    else:
        form = AuthenticationForm()
         
    return render(request, "Apk1/ingresar.html",{"form": form })

def salir(request):
    logout(request)
    return render(request,"Apk1/inicio.html")







