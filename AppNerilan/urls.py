from django.urls import path
from AppNerilan import views

urlpatterns = [
   
    path('', views.inicio, name="Inicio"), 
    path('empleado/', views.empleado, name="Empleado"),
    path('cliente/', views.cliente, name="Cliente"),
    path('finanzas/', views.finanzas, name="Finanzas"),
    path('empleadoFormulario/', views.empleadoFormulario, name="EmpleadoFormulario"),
    path('clienteFormulario/', views.clienteFormulario, name="ClienteFormulario"),
    path('finanzasFormulario/', views.finanzasFormulario, name="FinanzasFormulario"),
    path("busquedaemail/",views.busquedaemail,name="busquedaemail"),
    path("buscar/",views.buscar),
]

