from django.shortcuts import render, HttpResponse
from django.template.loader import get_template
from rest_framework import viewsets
from .serializer import RegistrosSerializer
from .models import Registros

def inicio(request):
    
    return render(request, "index.html")

def registrarse(request):

    return render(request, "registrarse.html")

def contacto(request):
    
    return render(request, "contacto.html")

def valores_criticos(request):
    
    return render(request, "valores_criticos.html")
    
def mostrar_datos(request):
    datos = Registros.objects.all() 
    return render(request, 'lecturas.html', {'datos': datos})

def filtrar_ubicacion(request):
    ubicacion = request.GET.get('ubicacion')
    if ubicacion: 
        datos = Registros.objects.filter(ubicacion__icontains=ubicacion)  
    else:
        datos = Registros.objects.all()
        
    return render(request, 'lecturas.html', {'datos': datos})

def filtrar_modulo(request):
    modulo = request.GET.get('modulo')
    if modulo: 
        datos = Registros.objects.filter(modulo__icontains=modulo)  
    else:
        datos = Registros.objects.all()
        
    return render(request, 'lecturas.html', {'datos': datos})


