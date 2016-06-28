from django.shortcuts import render, redirect
from .models import Paquete, Reservacion, Cliente
from .forms import DisponibiliddadForm, ClienteForm
from django.utils.dateparse import parse_date

# Create your views here.

def index(request):
    return render(request, 'index.html')

def disponibilidad(request):
    form = DisponibiliddadForm()
    if request.method == 'POST':
        form = DisponibiliddadForm(request.POST)
        if form.is_valid():
            fecha = form.cleaned_data['fecha']
            print(fecha)
            if Reservacion.objects.filter(fecha=fecha).exists():
                reservacion = Reservacion.objects.get(fecha=fecha)
                res = reservacion.paquete.id
                paquetes = Paquete.objects.all().exclude(id=res)
                context = {
                       'fecha': fecha,
                        'paquetes': paquetes,
                        'form': form,
                }
                return render(request, 'disponibilidad.html', context)
            else:
                paquetes = Paquete.objects.all().order_by('nombre')
                context = {
                    'fecha': fecha,
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
    form =  ClienteForm()
    if request.method == 'POST':
        if 'datos-personales' in request.POST:
            form =  ClienteForm(request.POST)
            paquet = request.POST.get('paquete', False)
            fecha = request.POST.get('fecha', False)
            if form.is_valid():
                form.save()
                ultimoUsuario = Cliente.objects.last()
                obtenerPaquete = Paquete.objects.get(id=paquet)
                nuevareserva = Reservacion(paquete=obtenerPaquete,cliente=ultimoUsuario, fecha=fecha)
                nuevareserva.save()
                ultimopk = Reservacion.objects.last()
                idpk = ultimopk.id
                return redirect('recibo', pk=idpk)

        if 'fecha-entrega' in request.POST:
            fecha = request.POST.get('fecha', False)
            context = {
                'fecha': fecha,
                'form': form,
                'paquete': paquete,
            }
            return render(request, 'datos_personales.html', context)

    context = {
        'form': form,
        'paquete': paquete,
    }
    return render(request, 'datos_personales.html', context)

def recibo(request, pk):
    ultimo = Reservacion.objects.get(pk=pk)
    return render(request, 'recibo.html', {'ultimo':ultimo})