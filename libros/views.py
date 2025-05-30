from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import LibroForm
from django.urls import reverse_lazy
from .models import Libro

class LibroCreateView(CreateView):
    model = Libro
    template_name = "libro_create.html"
    form_class = LibroForm
    success_url = reverse_lazy("libros")

    def form_valid(self, form):
        # Asignar el número de inventario de forma secuencial
        ultimo_numero = Libro.objects.latest('numero_Inventario').numero_Inventario if Libro.objects.exists() else 0
        form.instance.numero_Inventario = ultimo_numero + 1
        return super().form_valid(form)

# Create your views here.

def listaLibros(request):
    query = request.GET.get('buscar')
    if query:
        libros = Libro.objects.filter(titulo__icontains=query) | Libro.objects.filter(autor__icontains=query)
    else:
        libros = Libro.objects.all()
    
    return render(request, 'libros.html', {'libros': libros, 'query': query})

class LibroCreateView(CreateView):
    model = Libro
    template_name = "libro_create.html"
    form_class = LibroForm
    success_url = reverse_lazy("libros")

def libro_update(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('libros', pk=libro.pk)
    else:
        form = LibroForm(instance=libro)
    return render(request, 'libro_update.html', {'form': form})

class LibroUpdateView(UpdateView):
    model = Libro
    template_name = "libro_update.html"
    form_class = LibroForm
    success_url = reverse_lazy("libros")

class LibroDeleteView(DeleteView):
    model = Libro
    template_name = "libro_delete.html"
    success_url = reverse_lazy("libros")
        
def Busqueda(request):
    busqueda = request.GET.get("buscar")
    libros = Libro.objects.all()

    if busqueda:
        libros = Libro.objects.filter(
            Q(titulo__icontains = busqueda) |
            Q(autor__icontains = busqueda)
        ).distinct()


    return render(request,"libros.html",{'libros': libros})