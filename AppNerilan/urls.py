from django.urls import path
from AppNerilan import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
   
    path('', views.inicio, name="Inicio"), 
    path('empleado/', views.empleado, name="empleado"),
    path('finanzas/', views.finanzas, name="finanzas"),
    path('cliente/', views.cliente, name="cliente"),
    path("padre/",views.padre,name="padre"),
    path("buscar/",views.buscar, name="buscar"),
    path('login', views.login_request, name="Login"),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='AppNerilan/logout.html'), name='Logout'),
    path('editarPerfil', views.editarPerfil, name="editarPerfil"), 
    path('agregarAvatar', views.agregarAvatar,name="AgregarAvatar"),
    path("nohaydatos/",views.no_hay_datos, name="nohaydatos"),
    path('lista_articulos/', views.lista_articulos, name='lista_articulos'),
]
