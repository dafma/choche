from django.db import models

# Create your models here.


class Paquete(models.Model):
    nombre = models.CharField(max_length=20)
    personas = models.CharField(max_length=3)
    sillas = models.SmallIntegerField()
    cubresillas = models.SmallIntegerField("cubre sillas", null=True, blank=True)
    mesas = models.SmallIntegerField()
    manteles = models.SmallIntegerField()
    cubremanteles = models.SmallIntegerField()
    juego_loza = models.SmallIntegerField("Juegos de loza, vaso, plato, cubiertos", blank=True, null=True)
    precio = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=120)
    ciudad = models.CharField(max_length=150)
    direccion = models.TextField()
    codigo_postal = models.SmallIntegerField()
    telefono = models.IntegerField()
    email = models.EmailField()
    c_email = models.EmailField("Confirmar e-mail", )
    tyc = models.BooleanField("Terminos y condiciones",)

    def __str__(self):
        return self.nombre

class Reservacion(models.Model):
    paquete = models.ForeignKey(Paquete)
    cliente = models.ForeignKey(Cliente)
    fecha = models.DateField(unique=True)

    def __str__(self):
        return "%s, %s"% (self.paquete, self.cliente)

