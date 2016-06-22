from django.contrib import admin
from .models import Paquete, Cliente, Reservacion
# Register your models here.

@admin.register(Paquete)
class PaqueteAdmin(admin.ModelAdmin):
    pass


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    pass


@admin.register(Reservacion)
class ReservacionAdmin(admin.ModelAdmin):
    pass
