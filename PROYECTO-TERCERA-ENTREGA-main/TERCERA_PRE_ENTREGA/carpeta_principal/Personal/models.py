from django.db import models

# Create your models here.


class Personal(models.Model):
    nombre = models.CharField(max_length=230)
    numero_legajo = models.CharField(max_length=230)
    antiguedad = models.IntegerField(null=True)
    puesto = models.CharField(max_length=230)


class Inventario(models.Model):
    codigo = models.CharField(max_length=230)
    unidades = models.CharField(max_length=230)
    localizador =  models.IntegerField(null=True)


class Ventas(models.Model):
    codigo_de_producto=models.CharField(max_length=230)
    unidades = models.IntegerField(null=True)
    vendedor = models.CharField(max_length=230)
    descripcion= models.TextField()