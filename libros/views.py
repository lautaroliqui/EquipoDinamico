from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import LibroForm, PrestamoForm
from django.urls import reverse_lazy
# Create your views here.


def base(request):
    return render(request,"libros/base.html")


def libros(request):
    return render(request,"libros.html")

#def libros(request):
    Libros = Libro.objects.all()
    return render(request,"libros.html", {'libros': Libros})



class LibroCreateView(CreateView):
    model = Libro
    template_name = "libro_create.html"
    form_class = LibroForm
    success_url = reverse_lazy("libros")

class LibroUpdateView(UpdateView):
    model = Libro
    template_name = "libro_update.html"
    form_class = LibroForm
    success_url = reverse_lazy("libros")

class LibroDeleteView(DeleteView):
    model = Libro
    template_name = "libro_delete.html"
    success_url = reverse_lazy("libros")
        

def busqueda(request):
    return render(request,"busqueda.html")


def ModeloVista(request):
    busqueda = request.GET.get("buscar")
    libros = Libro.objects.all()

    if busqueda:
        libros = Libro.objects.filter(
            Q(titulo__icontains = busqueda) |
            Q(autor__icontains = busqueda)
        ).distinct()


    return render(request,"vistaLibros.html",{'libros': libros})


def vistaPrestamo(request):

    busqueda = request.GET.get("buscar")
    prestamos = Prestamo.objects.all()

    if busqueda:
        prestamos = Prestamo.objects.filter(
            Q(nombre__icontains = busqueda)
            ).distinct()
    return render(request,"vistaPrestamo.html",{"prestamos": prestamos})

class PrestamoCreateView(CreateView):
    model = Prestamo
    template_name = "prestamo.html"
    form_class = PrestamoForm
    success_url = reverse_lazy("prestamo")


class PrestamoDeleteView(DeleteView):
    model = Prestamo
    template_name = "prestamo_delete.html"
    success_url = reverse_lazy("vistaPrestamo")