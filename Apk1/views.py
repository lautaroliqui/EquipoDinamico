from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request,"base.html")

def inicio(request):
    return render(request,"inicio.html")

def AcercaDe(request):
    return render(request,"AcercaDe.html")

def contacto(request):
    return render(request,"contacto.html")