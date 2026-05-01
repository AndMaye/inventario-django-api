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
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Producto
from .serializers import ProductoSerializer

@api_view(['GET', 'POST'])
def productos_api(request):

    if request.method == 'GET':
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)  
    
@api_view(['DELETE'])
def eliminar_producto(request, id):
    try:
        producto = Producto.objects.get(id=id)
    except Producto.DoesNotExist:
        return Response({'error': 'No existe'}, status=404)

    producto.delete()
    return Response({'mensaje': 'Producto eliminado'})

@api_view(['PUT'])
def editar_producto(request, id):
    try:
        producto = Producto.objects.get(id=id)
    except Producto.DoesNotExist:
        return Response({'error': 'No existe'}, status=404)

    serializer = ProductoSerializer(producto, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors)