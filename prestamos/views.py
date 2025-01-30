from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import PrestamoForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Prestamo
from django.db.models import Q

# Create your views here.
def Prestamos(request): 
    busqueda = request.GET.get("buscar") 
    prestamos = Prestamo.objects.all() 
    if busqueda: prestamos = Prestamo.objects.filter( 
        Q(nombre__icontains = busqueda) | 
        Q(apellido__icontains = busqueda) | 
        Q(libro_solicitado__icontains = busqueda) ).distinct() 
    
    return render(request,"prestamos.html",{'prestamos': prestamos, 'query': busqueda})

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
    success_url = reverse_lazy("prestamos")