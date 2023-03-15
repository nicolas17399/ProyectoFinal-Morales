from django.db import models

# Create your models here.
class Empleado(models.Model):
    nombre=models.CharField(max_length=30)
    antiguedad=models.IntegerField()
    email=models.EmailField()

class Cliente(models.Model):
    nombre=models.CharField(max_length=30)
    formadepago=models.CharField(max_length=30)
    tienedeuda=models.BooleanField()

class Finanzas(models.Model):
    gastos=models.IntegerField()
    ganancias=models.IntegerField()
