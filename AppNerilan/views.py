from django.shortcuts import render
from AppNerilan.models import *
from django.http import HttpResponse, HttpResponseRedirect
from AppNerilan.forms import *

"""cliente = Cliente(nombre="Supermaren", formadepago="credito", tienedeuda=False)
cliente.save()"""

"""def cliente(self):
    cliente=Cliente.objects.get(nombre="Megamax",formadepago="Credito", tienedeuda=False)
    #cliente.save()
    documentoDeTexto=f"--->Cliente:{cliente.nombre},Cliente{cliente.formadepago},Cliente{cliente.tienedeuda}"
    return HttpResponse(documentoDeTexto)"""
def inicio(recuest):
    return render(recuest,"AppNerilan/inicio.html")
def padre(request):
    return render(request, 'AppNerilan/padre.html')
def empleado(recuest):
   return render(recuest,"AppNerilan/empleado.html")
def cliente(recuest):
   return render(recuest,"AppNerilan/cliente.html")
def finanzas(recuest):
   return render(recuest,"AppNerilan/finanzas.html")
def empleadoFormulario(request):
      return render(request,"AppNerilan/empleado.html")
def clienteFormulario(request):
      return render(request,"AppNerilan/cliente.html")
def finanzasFormulario(request):
      return render(request,"AppNerilan/finanzas.html")

def cliente(request):
      if request.method == 'POST':
      
            miFormulario1 =  ClienteFormulario(request.POST)
            print(miFormulario1)
            if miFormulario1.is_valid():
                 informacion=miFormulario1.cleaned_data
                 clientes=Cliente(nombre=informacion['nombre'], metododepago=informacion['metododepago'] , tienedeuda=informacion['tienedeuda'])
            clientes.save()
 
            return render(request, "AppNerilan/padre.html")
      else:
           miFormulario1=ClienteFormulario()
      return render(request,"AppNerilan/cliente.html",{"miFormulario1":miFormulario1})
def empleado(request):
      if request.method == 'POST':
            miFormulario2 =  EmpleadoFormulario(request.POST)
            print(miFormulario2)
            if miFormulario2.is_valid():
                  informacion=miFormulario2.cleaned_data
                  empleados=Empleado(nombre=informacion['nombre'],antiguedad=informacion['antiguedad'],email=informacion['email'])
                  empleados.save()
            return render(request, "AppNerilan/padre.html")
      else:
            miFormulario2=EmpleadoFormulario()
      return render(request,"AppNerilan/empleado.html",{"miFormulario2":miFormulario2})

def finanzas(request):
      if request.method == 'POST':
            miFormulario3 = FinanzasFormulario(request.POST)
            print(miFormulario3)
            if miFormulario3.is_valid():
                  informacion=miFormulario3.cleaned_data
                  finanzas=Finanzas(gastos=informacion['gastos'],antiguedad=informacion['ganancias'])
                  finanzas.save()
            return render(request, "AppNerilan/padre.html")
      else:
            miFormulario3=FinanzasFormulario()
      return render(request,"AppNerilan/finanzas.html",{"miFormulario3":miFormulario3})


#def busquedaemail(recuest):
 #  return render(recuest, "AppNerilan/padre.html")
def buscar(recuest):
    if 'email' in recuest.GET:
        #respuesta=f"Estoy buscando el email:{recuest.GET['email']}"
        email=recuest.GET['email']
        emple=Empleado.objects.filter(email__icontains=email)
        print(emple)
        return render(recuest,"AppNerilan/buscar.html",{"empleado":emple, "email":email})
    else:
         respuesta="No enviaste datos"
         return render(recuest,"AppNerilan/buscar.html",{"respuesta":respuesta})
    

""" <!-- <form method="post" action="{% url 'buscar/' %}">
            {% csrf_token %}
            <input type="text" name="busqueda">
            <button type="submit">Buscar</button>
        </form>-->
      
        <!--<form action="/AppNerilan/buscar" method="POST">{% csrf_token %}
            <input type="email" name="email" id="email">
            <input type="submit" value="buscar">
        </form>
            -->"""
    





