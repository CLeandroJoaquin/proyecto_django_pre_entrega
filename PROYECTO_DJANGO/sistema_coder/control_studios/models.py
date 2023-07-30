from django.db import models

# Create your models here.
class Curso(models.Model):
    #los atributos de a clase son las columnas de la table
    nombre= models.CharField(max_length=64)
    comision=models.IntegerField()
    def __str__ (self):
        return f"{self.nombre},{self.comision}"


class Estudiante(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    dni = models.CharField(max_length=32)
    fecha_nacimiento = models.DateField(null=True)
    def __str__ (self):
        return f"{self.nombre},{self.apellido}"



class Profesor(models.Model):
     nombre= models.CharField(max_length=256)
     apellido= models.CharField(max_length=256)
     email=models.EmailField(blank=True)
     dni= models.CharField(max_length=20)
     fecha_nacimiento= models.DateField(null=True)
     profesion=models.CharField(max_length=128)
     bio= models.TextField(blank=True)
     def __str__ (self):
        return f"{self.nombre},{self.apellido}"



class Entregable(models.Model):
     nombre= models.CharField(max_length=256)
     fecha_entrega= models.DateTimeField(auto_now_add=True)
     esta_aprobado= models.BooleanField(default=False)