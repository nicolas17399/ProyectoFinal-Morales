from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Empleado(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    nombre=models.CharField(max_length=30)
    antiguedadMeses=models.IntegerField()
    email=models.EmailField()
    recibo=models.FileField(upload_to='recibo/')
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Antiguedad en meses {self.antiguedadMeses} - E-Mail {self.email} - Recibo {self.recibo}"

class Cliente(models.Model):
    cliente = models.OneToOneField(User, on_delete=models.CASCADE)
    metododepago=models.CharField(max_length=30)
    tienedeuda=models.BooleanField(default=False)

    def __str__(self):
        return f"Nombre: {self.cliente} - Metododepago {self.metododepago} - Tienedeuda {self.tienedeuda}"


class Articulo(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    imagen = models.ImageField(upload_to='imagenes_articulos/', null=True, blank=True)

    def __str__(self):
        return self.nombre

class Eleccion(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    comentario = models.TextField(blank=True)
    fecha_eleccion = models.DateTimeField()
    terminado = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.cliente.user.username} eligió {self.cantidad} de {self.articulo.nombre}"

class Finanzas(models.Model):
    gastos=models.IntegerField()
    ganancias=models.IntegerField()
    def __str__(self):
        return f"Gastos: {self.gastos} - Ganancias {self.ganancias}"

class Avatar(models.Model):
   
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
 
    def __str__(self):
        return f"{self.user} - {self.imagen}"
    
"""Group.objects.get_or_create(name='grupo1')
Group.objects.get_or_create(name='grupo2')

class TuModelo(models.Model):
    ...
    
    class Meta:
        permissions = [
            ('ver_opcion1', 'Puede ver la opción 1'),
            ('ver_opcion2', 'Puede ver la opción 2'),
        ]"""
