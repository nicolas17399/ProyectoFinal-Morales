from django.urls import path
from .views import *

urlpatterns = [
    path('productos/', lista_productos, name='lista_productos'),
    path('editar/', editar_producto, name='editar_productos'),
    path('eliminar/', eliminar_peoducto, name='eliminar_productos'),
    ]