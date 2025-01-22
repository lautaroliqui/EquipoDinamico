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
    Libros = Libro.objects.all()
    return render(request,"libros/libros.html", {'libros': Libros})



class LibroCreateView(CreateView):
    model = Libro
    template_name = "libros/libro_create.html"
    form_class = LibroForm
    success_url = reverse_lazy("libros")

class LibroUpdateView(UpdateView):
    model = Libro
    template_name = "libros/libro_update.html"
    form_class = LibroForm
    success_url = reverse_lazy("libros")

class LibroDeleteView(DeleteView):
    model = Libro
    template_name = "libros/libro_delete.html"
    success_url = reverse_lazy("libros")



        

def busqueda(request):
    return render(request,"libros/busqueda.html")


def ModeloVista(request):
    busqueda = request.GET.get("buscar")
    libros = Libro.objects.all()

    if busqueda:
        libros = Libro.objects.filter(
            Q(titulo__icontains = busqueda) |
            Q(autor__icontains = busqueda)
        ).distinct()


    return render(request,"libros/vistaLibros.html",{'libros': libros})


def vistaPrestamo(request):

    busqueda = request.GET.get("buscar")
    prestamos = Prestamo.objects.all()

    if busqueda:
        prestamos = Prestamo.objects.filter(
            Q(nombre__icontains = busqueda)
            ).distinct()
    return render(request,"libros/vistaPrestamo.html",{"prestamos": prestamos})

class PrestamoCreateView(CreateView):
    model = Prestamo
    template_name = "libros/prestamo.html"
    form_class = PrestamoForm
    success_url = reverse_lazy("prestamo")


class PrestamoDeleteView(DeleteView):
    model = Prestamo
    template_name = "libros/prestamo_delete.html"
    success_url = reverse_lazy("vistaPrestamo")