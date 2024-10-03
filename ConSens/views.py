from django.shortcuts import render, HttpResponse
from django.template.loader import get_template
from rest_framework import viewsets
from .serializer import RegistrosSerializer
from .models import Registros

def inicio(request):
    
    return render(request, "index.html")

def registrarse(request):

    return render(request, "registrarse.html")

def lecturas(request):
    
   return render(request, "lecturas.html")

def contacto(request):
    
    return render(request, "contacto.html")

def valores_criticos(request):
    
    return render(request, "valores_criticos.html")

class RegistrosViewSet(viewsets.ModelViewSet):
    queryset = Registros.objects.all()
    serializer_class = RegistrosSerializer 