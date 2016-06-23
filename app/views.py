from django.shortcuts import render, redirect
from .models import Paquete, Reservacion
from .forms import DisponibiliddadForm, ClienteForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def disponibilidad(request):
    form = DisponibiliddadForm()
    if request.method == 'POST':
        form = DisponibiliddadForm(request.POST)
        if form.is_valid():
            dia = form.cleaned_data['fecha']
            print(dia)
            reservacion = Reservacion.objects.get(fecha=dia)
            res = reservacion.paquete.id
            paquetes = Paquete.objects.all().exclude(id=res)
            context = {
                    'paquetes': paquetes,
                    'form': form,
            }
            return render(request, 'disponibilidad.html', context)

    paquetes = Paquete.objects.all().order_by('nombre')
    context = {
        'paquetes': paquetes,
        'form': form,
    }
    return render(request, 'disponibilidad.html', context)

def datos_personales(request, pk):
    paquete = Paquete.objects.get(id=pk)
    form = ClienteForm()
    context = {
        'form': form,
        'paquete': paquete,
    }
    return render(request, 'datos_personales.html', context)