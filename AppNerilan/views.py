from django.shortcuts import render
from AppNerilan.models import *
from django.http import HttpResponse
from AppNerilan.forms import *

"""cliente = Cliente(nombre="Supermaren", formadepago="credito", tienedeuda=False)
cliente.save()"""

"""def cliente(self):
    cliente=Cliente.objects.get(nombre="Megamax",formadepago="Credito", tienedeuda=False)
    #cliente.save()
    documentoDeTexto=f"--->Cliente:{cliente.nombre},Cliente{cliente.formadepago},Cliente{cliente.tienedeuda}"
    return HttpResponse(documentoDeTexto)"""
#def inicio(recuest):
 #   return render(recuest,"AppNerilan/inicio.html")
def inicio(request):
    return render(request, 'AppNerilan/padre.html')
#def empleado(recuest):
 #   return render(recuest,"AppNerilan/empleado.html")
#def cliente(recuest):
 #   return render(recuest,"AppNerilan/cliente.html")
#def finanzas(recuest):
 #   return render(recuest,"AppNerilan/finanzas.html")

def empleadoFormulario(request):
      return render(request,"AppNerilan/empleadoFormulario.html")
def clienteFormulario(request):
      return render(request,"AppNerilan/clienteFormulario.html")
def finanzasFormulario(request):
      return render(request,"AppNerilan/finanzasFormulario.html")

def cliente(request):
      if request.method == 'POST':
      
            miFormulario =  ClienteFormulario(request,POST)
            print(miFormulario)
            if miFormulario.is_valid:
                 informacion=miFormulario.cleaned_data
                 clientes=Cliente(nombre=informacion['nombre'],formadepago=informacion['formadepago'],tienedeuda=informacion['tienedeuda'])
            clientes.save()
 
            return render(request, "AppNerilan/inicio.html")
      else:
           miFormulario=ClienteFormulario()
      return render(request,"AppNerilan/cliente.html",{"miFormulario":miFormulario})
#(request.post['nombre'],request.post['formadepago'],request.post['tienedeuda'])
def empleado(request):
      if request.method == 'POST':
            
            miFormulario =  EmpleadoFormulario(request,POST)
            print(miFormulario)
            if miFormulario.is_valid:
                  informacion=miFormulario.cleaned_data
                  empleados=Empleado(nombre=informacion['nombre'],antiguedad=informacion['antiguedad'],email=informacion['email'])
                  empleados.save()
            return render(request, "AppNerilan/inicio.html")
      else:
            miFormulario=EmpleadoFormulario()
      return render(request,"AppNerilan/empleado.html",{"miFormulario":miFormulario})

def finanzas(request):
      if request.method == 'POST':
            miFormulario = FinanzasFormulario(request,POST)
            print(miFormulario)
            if miFormulario.is_valid:
                  informacion=miFormulario.cleaned_data
                  finanzas=Finanzas(gastos=informacion['gastos'],antiguedad=informacion['ganancias'])
                  finanzas.save()
            return render(request, "AppNerilan/inicio.html")
      else:
            miFormulario=FinanzasFormulario()
      return render(request,"AppNerilan/finanzas.html",{"miFormulario":miFormulario})
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
    





