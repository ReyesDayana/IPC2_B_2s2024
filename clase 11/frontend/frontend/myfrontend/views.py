from django.shortcuts import render, redirect
import requests
# Create your views here.
def index(request):
    return render(request, 'index.html')


def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        response = requests.post('http://localhost:5000/api/login', json={'username': username, 'password': password})
        if response.status_code == 200:
            return redirect('upload_xml')
        else:
            return render(request, 'admin_login.html', {'error': 'Credenciales incorrectas'})
    return render(request, 'admin_login.html')

def upload_xml(request):
    if request.method== 'POST':
        if 'file' in request.FILES:
            file = request.FILES['file']
            xml_content = file.read().decode('utf-8')
            return render(request, 'upload_xml.html', {'xml_content': xml_content, 'editable': True})
        elif request.POST.get('xml_content'):
            xml_content = request.POST.get('xml_content')
            response = requests.post('http://localhost:5000/api/upload-xml', data={'xml_content': xml_content})
            if response.status_code == 200:
                return render(request, 'upload_xml.html', {'editable': False, 'success': 'Archivo procesado exitosamente'})
            else:
                return render(request, 'upload_xml.html', {'error': 'Error al procesar el archivo'})
    return render(request, 'upload_xml.html')

def ver_estadisticas(request):
    response = requests.get('http://localhost:5000/api/ventas')
    if response.status_code == 200:
        ventas = response.json().get('ventas', [])
        return render(request, 'ver_estadisticas.html', {'ventas': ventas})
    else:
        return render(request, 'ver_estadisticas.html', {'error': "Error al obtener las ventas"})

def productos(request):
    productos_disponibles = [
        {'nombre': 'Laptop', 'precio': 15000},
        {'nombre': 'Smartphone', 'precio': 8000},
        {'nombre': 'Tablet', 'precio': 5000},
        {'nombre': 'Monitor', 'precio': 3000},
        {'nombre': 'Teclado Mecánico', 'precio': 500},
    ]
    if request.method == 'POST':
        producto = request.POST.get('producto')
        if producto:
            response = requests.post('http://localhost:5000/api/agregar-venta', json={'producto': producto, 'cantidad': 1})
            if response.status_code == 200:
                  return render(request, 'productos.html', {'productos': productos_disponibles, 'success': 'Producto agregado a la venta exitosamente'})
            else:
                return render(request, 'productos.html', {'productos': productos_disponibles, 'error': 'Error al agregar el producto a la venta'})
    return render(request, 'productos.html', {'productos': productos_disponibles})