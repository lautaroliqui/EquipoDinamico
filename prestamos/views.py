from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import PrestamoForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Prestamo

# Create your views here.

def listaPrestamos(request):
    query = request.GET.get('buscar')
    if query:
        prestamos = Prestamo.objects.filter(nombre__icontains=query) | Prestamo.objects.filter(apellido__icontains=query)
    else:
        prestamos = Prestamo.objects.all()
    
    return render(request, 'prestamo.html', {'prestamos': prestamos, 'query': query})

class PrestamoCreateView(CreateView):
    model = Prestamo
    template_name = "prestamo_create.html"
    form_class = PrestamoForm
    success_url = reverse_lazy("prestamos")

class PrestamoUpdateView(UpdateView):
    model = Prestamo
    template_name = "prestamo_update.html"
    form_class = PrestamoForm
    success_url = reverse_lazy("prestamos")

class PrestamoDeleteView(DeleteView):
    model = Prestamo
    template_name = "prestamo_delete.html"
    success_url = reverse_lazy("vistaPrestamo")