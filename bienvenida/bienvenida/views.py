from django.http import HttpResponse

from django.shortcuts import render
from . import models

def inicio(request):
    return HttpResponse("Hola mundo desde Django")


# Redirigir la raíz al listado de productos
from django.shortcuts import redirect
def mostrar_bienvenida(request):
    return redirect('producto_list')

def lista_productos(request):
    productos = models.Producto.objects.all()
    return render(request, 'productos/lista.html', {'productos': productos})