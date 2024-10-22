from django.shortcuts import render, redirect
import requests

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Hacer solicitud al backend Flask
        response = requests.post('http://127.0.0.1:5000/api/login', json={
            'username': username,
            'password': password
        })
        
        if response.status_code == 200:
            return redirect('success')  # Redirigir a la página de éxito si es correcto
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    
    return render(request, 'login.html')

def success(request):
    return render(request, 'success.html')
