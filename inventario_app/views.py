from django.shortcuts import render, redirect
from .models import Producto

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})

def crear_producto(request):
    if request.method == "POST":
        nombre = request.POST['nombre']
        precio = request.POST['precio']
        stock = request.POST['stock']
        descripcion = request.POST['descripcion']

        Producto.objects.create(
            nombre=nombre,
            precio=precio,
            stock=stock,
            descripcion=descripcion
        )
        return redirect('lista_productos')

    return render(request, 'crear_producto.html')
def editar_producto(request, id):
    producto = Producto.objects.get(id=id)

    if request.method == "POST":
        producto.nombre = request.POST['nombre']
        producto.precio = request.POST['precio']
        producto.stock = request.POST['stock']
        producto.descripcion = request.POST['descripcion']
        producto.save()
        return redirect('lista_productos')

    return render(request, 'editar_producto.html', {'producto': producto})


def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('lista_productos')