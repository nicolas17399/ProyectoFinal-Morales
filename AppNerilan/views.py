from django.shortcuts import render
from AppNerilan.models import *
from django.http import HttpResponse
from AppNerilan.forms import *

"""cliente = Cliente(nombre="Supermaren", formadepago="credito", tienedeuda=False)
cliente.save()"""

def cliente(self):
    cliente=Cliente.objects.get(nombre="Megamax",formadepago="Credito", tienedeuda=False)
    #cliente.save()
    documentoDeTexto=f"--->Cliente:{cliente.nombre},Cliente{cliente.formadepago},Cliente{cliente.tienedeuda}"
    return HttpResponse(documentoDeTexto)
#def inicio(recuest):
 #   return render(recuest,"AppNerilan/inicio.html")
def inicio(request):
    return render(request, 'AppNerilan/padre.html')
def empleado(recuest):
    return render(recuest,"AppNerilan/empleado.html")
def cliente(recuest):
    return render(recuest,"AppNerilan/cliente.html")
def finanzas(recuest):
    return render(recuest,"AppNerilan/finanzas.html")

def empleadoFormulario(request):
      return render(request,"AppNerilan/empleadoFormulario.html")
def clienteFormulario(request):
      return render(request,"AppNerilan/clienteFormulario.html")
def finanzasFormulario(request):
      return render(request,"AppNerilan/finanzasFormulario.html")

def clienteFormulario(request):
      if request.method == 'POST':
      
            cliente =  Cliente(request.post['nombre'],request.post['formadepago'],request.post['tienedeuda'])
 
            cliente.save()
 
            return render(request, "AppNerilan/inicio.html")
 
      return render(request,"AppNerilan/clienteFormulario.html")

def empleadoFormulario(request):
      if request.method == 'POST':
      
            empleado =  Empleado(request.post['nombre'],request.post['antiguedad'],request.post['email'])
 
            empleado.save()
 
            return render(request, "AppNerilan/inicio.html")
 
      return render(request,"AppNerilan/empleadoFormulario.html")

def finanzasFormulario(request):
      if request.method == 'POST':
      
            finanzas=  Finanzas(request.post['gastos'],request.post['ganancias'])
 
            finanzas.save()
 
            return render(request, "AppNerilan/inicio.html")
 
      return render(request,"AppNerilan/finanzasFormulario.html")
"""
from AppNerilan.forms import ClienteFormulario
 
def clienteFormulario(request):
 
      if request.method == "POST":
 
            miFormulario = ClienteFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  cliente = Cliente(nombre=informacion["nombre"], formadepago=informacion["formadepago"], tienedeuda=informacion["tienedeuda"])
                  cliente.save()
                  return render(request, "AppNerilan/inicio.html")
      else:
            miFormulario = ClienteFormulario()
 
      return render(request, "AppNerilan/clienteFormulario.html", {"miFormulario": miFormulario})"""

def busquedaemail(recuest):
    return render(recuest, "AppNerilan/busquedaemail.html")
def buscar(recuest):
    if email in recuest.GET['email']:
        #respuesta=f"Estoy buscando el email:{recuest.GET['email']}"
        email=recuest.GET['email']
        emple=Empleado.objects.filters(email__icontains=email)
        return render(recuest,"AppNerilan/ResultadosPorBusqueda.html",{"empleado":emple, "email":email})
    else:
         respuesta="No enviaste datos"
         return HttpResponse(respuesta)
    





