from django.shortcuts import render
from app.models import *
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

# Create your views here.

class ReservacionList(ListView):
    model = Reservacion
    template_name = 'reservaciones-admin.html'


class ClientesList(ListView):
    model = Cliente
    template_name = 'clientes-admin.html'

class PaqueteList(ListView):
    model = Paquete
    template_name = 'paquete-admin.html'

class PaqueteCreation(CreateView):
    model = Paquete
    template_name = "paquetes/crear_paquete.html"
    success_url = reverse_lazy('administrador:paquetes')
    fields = ['nombre', 'personas', 'sillas', 'cubresillas', 'mesas', 'manteles', 'cubremanteles', 'juego_loza', 'precio']

class PaqueteUpdate(UpdateView):
    model = Paquete
    success_url = reverse_lazy('administrador:paquetes')
    fields = ['nombre', 'personas', 'sillas', 'cubresillas', 'mesas', 'manteles', 'cubremanteles', 'juego_loza', 'precio']


class PaqueteEdit(DeleteView):
    model = DeleteView
    success_url = reverse_lazy('administrador:paquetes')