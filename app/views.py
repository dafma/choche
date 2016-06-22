from django.shortcuts import render
from .models import Paquete, Cliente, Reservacion
from .forms import DisponibiliddadForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def disponibilidad(request):
    form = DisponibiliddadForm()
    if request.method == 'POST':
        if form.is_valid():
            dia = form.cleaned_data['fecha']
            reservacion  = Reservacion.objects.all().exclude(fecha = dia)
            context = {
                'paquetes': paquetes,
                'form': form,
            }
            return render(request, 'disponibilidad.html')

    paquetes = Paquete.objects.all().order_by('nombre')
    context = {
        'paquetes': paquetes,
        'form': form,
    }
    return render(request, 'disponibilidad.html', context)