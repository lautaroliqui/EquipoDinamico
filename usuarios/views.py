from django.shortcuts import redirect, render
from django.shortcuts import render
from .forms import *
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout

# Create your views here.

def registro(request):
    if request.method == "POST":
        form = registrarUsuarioForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            form.save()
            return redirect("inicio")
        else:
            return render(request, "registro.html", {"form": form, "mensajeIncorrecto": "Error al crear el usuario"})
    else:
        form = registrarUsuarioForm()
    return render(request, "registro.html", {"form": form})


def ingresar(request):
    if request.method == "POST":
        form = ingresarForm(request,data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            clave = form.cleaned_data.get("password")
            usuario1 = authenticate(username = usuario, password = clave)#trae un usuario de la base
            if usuario1 is not None:
                login(request, usuario1)
                return redirect('inicio')
            else:
                return render(request,"ingresar.html", {
                    "mensajeIncorrecto": "Usuario o contraseña incorrectos.",
                    "form": form
                })
        else:
               return render(request, "ingresar.html", {
                "mensajeIncorrecto": "Usuario o contraseña incorrectos.",
                "form": form
            })
    else:
        form = ingresarForm()
         
    return render(request, "ingresar.html", {
        "form": form
    })

def salir(request):
    logout(request)
    return render(request,"inicio.html")
