from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hola_mundo(request):
    return HttpResponse("Hola mundo")

def saludo(request):
    return HttpResponse("Saludos mundo")