from django.urls import path
from AppNerilan import views

urlpatterns = [
   
    path('', views.inicio, name="Inicio"), 
    path('empleado/', views.empleado, name="empleado"),
    #path('cliente/', views.cliente, name="Cliente"),
    path('finanzas/', views.finanzas, name="finanzas"),
    #path('empleadoFormulario/', views.empleadoFormulario, name="EmpleadoFormulario"),
    path('cliente/', views.cliente, name="cliente"),
    #path('finanzasFormulario/', views.finanzasFormulario, name="FinanzasFormulario"),
    path("padre/",views.padre,name="padre"),
    path("buscar/",views.buscar, name="buscar"),
]

