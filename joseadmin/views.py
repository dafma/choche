from django.shortcuts import render
from app.models import *
from django.views.generic import ListView

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

