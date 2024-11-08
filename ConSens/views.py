from django.shortcuts import render
from .models import Registros, ValorCriticoTemperatura, ValorCriticoHumedad, ValorCriticoPresion
from django.core.paginator import Paginator

def inicio(request):
    
    return render(request, "index.html")

def registrarse(request):

    return render(request, "registrarse.html")

def quienes_somos(request):
    
    return render(request, "quienes_somos.html")
    
def mostrar_lecturas(request):
    """Devuelve todos los datos de la entidad 'Registros'."""
    datos = Registros.objects.all() 
    return render(request, 'lecturas.html', {'datos': datos})

def filtrar_lecturas(request):
    """Devuelve los datos de la entidad 'Registros' filtrando por ubicación, módulo y rango de fechas."""
    ubicacion = request.GET.get('ubicacion').strip()
    modulo = request.GET.get('modulo').strip()
    fecha_max = request.GET.get('fecha_max')
    fecha_min = request.GET.get('fecha_min')

    datos = Registros.objects.all()
    
    # Filtra por ubicación
    if ubicacion:
        datos = datos.filter(ubicacion__icontains=ubicacion)
    
    # Filtra por módulo
    if modulo:
        datos = datos.filter(modulo__icontains=modulo)
    
    # Filtra por rango de fechas
    if fecha_min and fecha_max:
        datos = datos.filter(fecha__gte=fecha_min, fecha__lte=fecha_max)
        
    return render(request, 'lecturas.html', {'datos': datos})

def valores_criticos_temperatura(request):
    """Devuelve todos los datos de la entidad 'ValorCriticoTemperatura'."""
    valores = ValorCriticoTemperatura.objects.all() 
    return render(request, 'valores_criticos_temp.html', {'valores': valores})

def filtrar_temp(request):
    """Devuelve los datos de la entidad 'ValorCriticoTemperatura' filtrando por módulo, usuario y fecha."""
    modulo = request.GET.get('modulo').strip()
    usuario = request.GET.get('usuario').strip()
    fecha =request.GET.get('fecha')

    valores = ValorCriticoTemperatura.objects.all()
    
    # Filtra por módulo
    if modulo:
        valores = valores.filter(modulo__icontains=modulo)
        
    # Filtra por usuario
    if usuario:
        valores = valores.filter(valores__icontains=usuario)
        
    # Filtra por fecha especifica
    if fecha:
        valores = valores.filter(fecha__date=fecha)

    return render(request, 'valores_criticos_temp.html', {'valores': valores})

def valores_criticos_humedad(request):
    """Devuelve todos los datos de la entidad 'ValorCriticoHumedad'."""
    valores = ValorCriticoHumedad.objects.all() 
    return render(request, 'valores_criticos_hum.html', {'valores': valores})

def filtrar_hum(request):
    """Devuelve los datos de la entidad 'ValorCriticoHumedad' filtrando por módulo, usuario y fecha."""
    modulo = request.GET.get('modulo').strip()
    usuario = request.GET.get('usuario').strip()
    fecha =request.GET.get('fecha')
    
    valores = ValorCriticoHumedad.objects.all()
    
    # Filtra por módulo
    if modulo:
        valores = valores.filter(modulo__icontains=modulo)
        
    # Filtra por usuario
    if usuario:
        valores = valores.filter(valores__icontains=usuario)
        
    # Filtra por fecha especifica
    if fecha:
        valores = valores.filter(fecha__date=fecha)

    return render(request, 'valores_criticos_hum.html', {'valores': valores})

def valores_criticos_presion(request):
    """Devuelve todos los datos de la entidad 'ValorCriticoPresion'."""
    valores = ValorCriticoPresion.objects.all()
    return render(request, 'valores_criticos_pres.html', {'valores': valores})

def filtrar_pres(request):
    """Devuelve los datos de la entidad 'ValorCriticoPresion' filtrando por módulo, usuario y fecha."""
    modulo = request.GET.get('modulo').strip()
    usuario = request.GET.get('usuario').strip()
    fecha =request.GET.get('fecha')
    
    valores = ValorCriticoPresion.objects.all()
    
    # Filtra por módulo
    if modulo:
        valores = valores.filter(modulo__icontains=modulo)
        
    # Filtra por usuario
    if usuario:
        valores = valores.filter(valores__icontains=usuario)
        
    # Filtra por fecha especifica
    if fecha:
        valores = valores.filter(fecha__date=fecha)

    return render(request, 'valores_criticos_pres.html', {'valores': valores})
