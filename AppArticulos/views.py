from django.shortcuts import render
from .models import Producto
from .forms import ProductoForm
from django.shortcuts import render, redirect, get_object_or_404

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})


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

def eliminar_peoducto(request, id_articulo):
    producto = get_object_or_404(Producto, id=id_articulo)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_producto')
    return render(request, 'AppArticulos/eliminar_producto.html', {'producto': producto})
