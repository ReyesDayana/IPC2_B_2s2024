from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Producto
# Create your views here.
def lista_productos(request):
    productos = ['Laptop', 'SmartPhone', 'Tablet', 'Auriculares']
    salida = "<h1>Lista de Productos</h1>\n"
    salida += "<ul>\n"
    for producto in productos:
        salida += f"<li>{producto}</li>\n"
    salida += "</ul>"
    return HttpResponse(salida)

def listados_productos(request):
    productos = ['Laptop', 'SmartPhone', 'Tablet', 'Reloj']
    return render(request, 'productos/lista_productos.html', {'productos':productos })

def producto(request):
    return HttpResponse("Esta es la url principal de productos")



class ListaProductosView(ListView):
    model = Producto
    template_name = 'productos/productos_lista.html'
    context_object_name = 'productos'