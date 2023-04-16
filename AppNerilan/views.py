from django.shortcuts import *
from AppNerilan.models import *
from django.http import HttpResponse, HttpResponseRedirect
from AppNerilan.forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User,Group
from django.utils import timezone

default_value = timezone.now

#from django.contrib.auth.mixins import LoginRequiredMixin

#class ClaseQueNecesitaLogin (LoginRequiredMixin):
 #     pass
@login_required
def inicio(request):
    avatares=Avatar.objects.filter(user=request.user.id)
    print(avatares[0].imagen.url)
    return render(request,"AppNerilan/inicio.html",{"url":avatares[0].imagen.url})
def padre(request):
    return render(request, 'AppNerilan/padre.html')
def empleado(request):
   return render(request,"AppNerilan/empleado.html")
def cliente(request):
   return render(request,"AppNerilan/cliente.html")
def finanzas(request):
   return render(request,"AppNerilan/finanzas.html")
def no_hay_datos(request):
    return render(request, "AppNerilan/nohaydatos.html")
def acercademi(request):
    return render(request, "AppNerilan/acercademi.html")

def cliente(request):
      if request.method == 'POST':
      
            miFormulario1 =  ClienteFormulario(request.POST)
            print(miFormulario1)
            if miFormulario1.is_valid():
                 informacion=miFormulario1.cleaned_data
                 clientes=Cliente(cliente=request.user, metododepago=informacion['metododepago'] , tienedeuda=informacion['tienedeuda'])
            clientes.save()
 
            return render(request, "AppNerilan/padre.html")
      else:
           miFormulario1=ClienteFormulario()
      return render(request,"AppNerilan/cliente.html",{"miFormulario1":miFormulario1})

def lista_articulos(request):
    articulos = Articulo.objects.all()
    return render(request, 'AppNerilan/lista_articulos.html', {'articulos': articulos})

@login_required
def crear_eleccion(request, articulo_id):
    articulo = get_object_or_404(Articulo, pk=articulo_id)
    cliente = request.user.cliente
    if cliente is None:
        # El usuario no tiene un cliente asociado, redirigir a una página de error o crear un cliente nuevo
        return redirect('nohaydatos')
    if request.method == 'POST':
        cantidad = request.POST['cantidad']
        comentario = request.POST['comentario']
        fecha_eleccion = timezone.now()
        eleccion = Eleccion(cliente=cliente, articulo=articulo, cantidad=cantidad, comentario=comentario, fecha_eleccion=fecha_eleccion)
        eleccion.save()
        return redirect('articulos')
    else:
        return render(request, 'AppNerilan/elegir_cantidad.html', {'articulo': articulo})
@login_required
def editar_eleccion(request, eleccion_id):
    eleccion = get_object_or_404(Eleccion, pk=eleccion_id)
    if request.method == 'POST':
        comentario = request.POST['comentario']
        eleccion.comentario = comentario
        eleccion.save()
        return redirect('pedidos_cliente')
    else:
        return render(request, 'AppNerilan/editar_eleccion.html', {'eleccion': eleccion})

def marcar_como_terminado(request, eleccion_id):
    eleccion = get_object_or_404(Eleccion, pk=eleccion_id)
    eleccion.terminado = True
    eleccion.save()
    return redirect('pedidos_admin')
"""
#@login_required
#def empleado(request):
    if request.method == 'POST':
        miFormulario2 =  EmpleadoFormulario(request.POST, request.FILES)
        if miFormulario2.is_valid():
            informacion = miFormulario2.cleaned_data
            empleados = Empleado(user=request.user,
                                 nombre=informacion['nombre'],
                                 antiguedadMeses=informacion['antiguedadMeses'],
                                 email=informacion['email'],
                                 recibo=request.FILES['recibo'])
            empleados.save()
        return redirect('empleado')
    else:
        if request.user.is_staff:
            # Si el usuario es un administrador, obtener todos los empleados
            empleados = Empleado.objects.all()
        else:
            # Si el usuario no es un administrador, obtener solo su propio empleado
            empleados = Empleado.objects.filter(userid=request.user).first()
        miFormulario2 = EmpleadoFormulario()
        contexto = {"miFormulario2": miFormulario2, "empleados": empleados}
        return render(request, "AppNerilan/empleado.html", contexto)


#def empleado(request):
      if request.method == 'POST':
            miFormulario2 =  EmpleadoFormulario(request.POST, request.FILES)
            print(miFormulario2)
            if miFormulario2.is_valid():
                  informacion=miFormulario2.cleaned_data
                  empleados=Empleado(user=request.user,
                                     nombre=informacion['nombre'],
                                     antiguedadMeses=informacion['antiguedad'],
                                     email=informacion['email'],
                                     recibo=request.FILES['recibo'])
                  empleados.save()
            return render(request, "leerempleado")
      else:
            miFormulario2=EmpleadoFormulario()
      return render(request,"AppNerilan/empleado.html",{"miFormulario2":miFormulario2})


#def leerempleado(request):
    if request.user.is_staff:
        # Si el usuario es un administrador, obtener todos los empleados
        empleados = Empleado.objects.all()
        contexto = {"empleados": empleados}
        return render(request, "AppNerilan/empleado.html", contexto)
    else:
        # Si el usuario no es un administrador, obtener solo su propio empleado
        empleado = Empleado.objects.filter(user_id=request.user.id).first()
        if empleado:
            # Si se encontró al menos un empleado, renderizar la plantilla "empleado.html"
            contexto = {"empleados": [empleado]}
            return render(request, "AppNerilan/empleado.html", contexto)
        else:
            # Si no se encontraron empleados, redirigir a la página "no_hay_datos"
            return redirect("no_hay_datos")
 """
@login_required
def empleado(request):
    # Si el usuario es un administrador, obtener todos los empleados
    if request.user.is_staff:
        empleados = Empleado.objects.all()
    # Si el usuario no es un administrador, obtener solo su propio empleado
    else:
        empleado = Empleado.objects.filter(user=request.user).first()
        if empleado:
            empleados = [empleado]
        else:
            return redirect("nohaydatos")

    contexto = {"empleados": empleados}
    return render(request, "AppNerilan/empleado.html", contexto)
@login_required
def subirnuevorecibo(request):
    if request.method == 'POST':
        miFormulario2 = EmpleadoFormulario(request.POST, request.FILES)
        if miFormulario2.is_valid():
            informacion = miFormulario2.cleaned_data
            empleados = Empleado(user=request.user,
                                nombre=informacion['nombre'],
                                antiguedadMeses=informacion['antiguedad'],
                                email=informacion['email'],
                                recibo=request.FILES['recibo'])
            empleados.save()
            return redirect('leerempleado')
    else:
        miFormulario2 = EmpleadoFormulario()
    return render(request, "AppNerilan/subirnuevorecibo.html", {"miFormulario2": miFormulario2})
              
"""@login_required
def leerempleado(request):
    if request.user.is_staff:
        # Si el usuario es un administrador, obtener todos los empleados
        empleado = Empleado.objects.all()
    else:
        # Si el usuario no es un administrador, buscar su empleado específico
        empleado = Empleado.objects.filter(user=request.user).first()

        # Si no se encontró un empleado específico, redirigir a la página "no_hay_datos"
        if not empleado:
            return redirect("no_hay_datos")
        
    # Renderizar la plantilla "empleado.html" con los empleados encontrados
    contexto = {"empleados": empleado}
    return render(request, "AppNerilan/empleado.html", contexto)
"""
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

def agregarAvatar(request):
      if request.method == 'POST':
      
            miFormulario4 =  AvatarFormulario(request.POST,request.FILES)
            print(miFormulario4)
            if miFormulario4.is_valid():
                 u=User.objects.get(username=request.user)
                 avatar=Avatar(user=u, imagen=miFormulario4.cleaned_data['imagen'])
            avatar.save()
 
            return render(request, "AppNerilan/inicio.html")
      else:
           miFormulario4=AvatarFormulario()
      return render(request,"AppNerilan/agregarAvatar.html",{"miFormulario4":miFormulario4})


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
    
def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contraseña)

            if user is not None:
                login(request, user)

                return render(request, "AppNerilan/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "AppNerilan/inicio.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "AppNerilan/inicio.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "AppNerilan/login.html", {"form": form})

def logout_view(request):
    # código de logout...
    return redirect('Login')
"""
# Vista de registro
def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppNerilan/inicio.html" ,  {"mensaje":"Usuario Creado :)"})

      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"AppNerilan/register.html" ,  {"form":form})
"""
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Crear el usuario
            user = User.objects.create_user(
                form.cleaned_data['username'],
                form.cleaned_data['email'],
                form.cleaned_data['password1'],
                **{
                    'last_name': form.cleaned_data['last_name'],
                    'first_name': form.cleaned_data['first_name']
                }
            )
            # Agregar al grupo correspondiente
            if form.cleaned_data['user_type'] == 'client':
                group = Group.objects.get(name='Cliente')
                group.user_set.add(user)
            elif form.cleaned_data['user_type'] == 'employee':
                group = Group.objects.get(name='Empleado')
                group.user_set.add(user)

            return redirect('Login')
    else:
        form = UserRegisterForm()

    return render(request, 'AppNerilan/register.html', {'form': form})


@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario5 = UserEditForm(request.POST)
        if miFormulario5.is_valid():
            informacion = miFormulario5.cleaned_data


            usuario.email = informacion['email']
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']
            if informacion['password1'] == informacion['password2']:
                usuario.password = make_password(informacion['password1'])
                usuario.save()
            else:
                return render(request, 'inicio.html', {'mensaje':'Contrasena incorrecta'})


            return render(request, 'inicio.html')
    else:
        miFormulario5 = UserEditForm(initial={'email':usuario.email})


    return render(request, "AppNerilan/editarPerfil.html", {"miFormulario5":miFormulario5, "usuario":usuario})


"""
<!--{% if request.user.has_perm('AppNerilan.ver_opcion1') %}
                <li><a href="{% url 'vista_opcion1' %}">Opción 1</a></li>
            {% endif %}
            {% if request.user.has_perm('AppNerilan.ver_opcion2') %}
                <li><a href="{% url 'vista_opcion2' %}">Opción 2</a></li>
            {% endif %}-->
@login_required
def vista_general(request):
    return render(request, 'vista_general.html')

@login_required
@permission_required('AppNerilan.ver_opcion1', raise_exception=True)
@user_passes_test(lambda u: u.groups.filter(name='grupo1').exists())
def vista_opcion1(request):
    return render(request, 'vista_opcion1.html')

@login_required
@permission_required('AppNerilan.ver_opcion2', raise_exception=True)
@user_passes_test(lambda u: u.groups.filter(name='grupo2').exists())
def vista_opcion2(request):
    return render(request, 'vista_opcion2.html')
"""

"""{% if miFormulario.errors %}
        <p style="color: red;"> Estan mal los datos, revisar</p>
        {% endif %}
        <form action="" method="POST" enctype="multipart/form-data">{% csrf_token %}
            <table>
                {{ miFormulario2.as_table}}
            </table>
            <input type="submit" value="Enviar">
        </form>"""

from django.contrib.auth.models import Group

nuevo_grupo, creado = Group.objects.get_or_create(name='Client')
nuevo_grupo, creado = Group.objects.get_or_create(name='Employee')