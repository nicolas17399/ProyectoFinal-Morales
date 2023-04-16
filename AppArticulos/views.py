from django.shortcuts import *
from .models import Producto
from .forms import ProductoForm
from django.template.context_processors import dirs


def lista_productos(request):
    producto = Producto.objects.all()
    options = {
        'dirs': ['AppArticulos/templates'],
        'producto': producto
    }
    return render(request, 'lista_productos.html', options)

def editar_producto(request, id_producto):
    producto = get_object_or_404(Producto, id=id_producto)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'AppArticulos/editar_producto.html', {'form': form})

def eliminar_producto(request, id_articulo):
    producto = get_object_or_404(Producto, id=id_articulo)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'AppArticulos/eliminar_producto.html', {'producto': producto})
