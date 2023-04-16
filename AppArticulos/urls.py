from django.urls import path
from .views import *

urlpatterns = [
    path('', lista_productos, name='lista_productos'),
    path('editar/<int:id_producto>/', editar_producto, name='editar_producto'),
    path('eliminar/<int:id_articulo>/', eliminar_producto, name='eliminar_producto'),
]