from django.shortcuts import render
from .models import Registros, ValorCriticoTemperatura, ValorCriticoHumedad, ValorCriticoPresion, Modulo
from django.db.models import Max
from django.core.paginator import Paginator

def quienes_somos(request):
    return render(request, "quienes_somos.html")
    
def mostrar_lecturas(request):
    """Devuelve todos los datos de la entidad 'Registros'."""
    datos = Registros.objects.all() 
    
    paginator = Paginator(datos, 1)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'lecturas.html', {'datos': page_obj})

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
        datos = datos.filter(modulo__nombre__icontains=modulo)
    
    # Filtra por rango de fechas
    if fecha_min and fecha_max:
        datos = datos.filter(fecha__gte=fecha_min, fecha__lte=fecha_max)
    
    paginator = Paginator(datos, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'lecturas.html', {'datos': page_obj})

def ultimas_lecturas(request):
    """Devuelve la ultima lectura de cada modulo registrado"""
    ultimos_registros_ids = (Registros.objects.values('modulo').annotate(ultimo_id=Max('id')).values_list('ultimo_id', flat=True))
    # Filtrar solo los registros que correspondan a esos últimos IDs
    ultimos_registros = Registros.objects.filter(id__in=ultimos_registros_ids)

    return render(request, 'index.html', {'ultimos_registros': ultimos_registros} )
    
def valores_criticos_temperatura(request):
    """Devuelve todos los datos de la entidad 'ValorCriticoTemperatura'."""
    valores = ValorCriticoTemperatura.objects.all().order_by("-fecha", "-hora")
    
    paginator = Paginator(valores, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'valores_criticos_temp.html', {'valores': page_obj})

def filtrar_temp(request):
    """Devuelve los datos de la entidad 'ValorCriticoTemperatura' filtrando por módulo, usuario y fecha."""
    modulo = request.GET.get('modulo').strip()
    usuario = request.GET.get('usuario').strip()
    fecha =request.GET.get('fecha')

    valores = ValorCriticoTemperatura.objects.all().order_by("-fecha", "-hora")
    
    # Filtra por módulo
    if modulo:
        valores = valores.filter(modulo__nombre__icontains=modulo)
        
    # Filtra por usuario
    if usuario:
        valores = valores.filter(usuario__username__icontains=usuario)
        
    # Filtra por fecha especifica
    if fecha:
        valores = valores.filter(fecha__date=fecha)

    paginator = Paginator(valores, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'valores_criticos_temp.html', {'valores': page_obj})

def valores_criticos_humedad(request):
    """Devuelve todos los datos de la entidad 'ValorCriticoHumedad'."""
    valores = ValorCriticoHumedad.objects.all().order_by("-fecha", "-hora")
    
    paginator = Paginator(valores, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'valores_criticos_hum.html', {'valores': page_obj})

def filtrar_hum(request):
    """Devuelve los datos de la entidad 'ValorCriticoHumedad' filtrando por módulo, usuario y fecha."""
    modulo = request.GET.get('modulo').strip()
    usuario = request.GET.get('usuario').strip()
    fecha =request.GET.get('fecha')
    
    valores = ValorCriticoHumedad.objects.all().order_by("-fecha", "-hora")
    
    # Filtra por módulo
    if modulo:
        valores = valores.filter(modulo__nombre__icontains=modulo)
        
    # Filtra por usuario
    if usuario:
        valores = valores.filter(usuario__username__icontains=usuario)
        
    # Filtra por fecha especifica
    if fecha:
        valores = valores.filter(fecha__date=fecha)

    paginator = Paginator(valores, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'valores_criticos_hum.html', {'valores': page_obj})

def valores_criticos_presion(request):
    """Devuelve todos los datos de la entidad 'ValorCriticoPresion'."""
    valores = ValorCriticoPresion.objects.all().order_by("-fecha", "-hora")
    
    paginator = Paginator(valores, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'valores_criticos_pres.html', {'valores': page_obj})

def filtrar_pres(request):
    """Devuelve los datos de la entidad 'ValorCriticoPresion' filtrando por módulo, usuario y fecha."""
    modulo = request.GET.get('modulo').strip()
    usuario = request.GET.get('usuario').strip()
    fecha =request.GET.get('fecha')
    
    valores = ValorCriticoPresion.objects.all().order_by("-fecha", "-hora")
    
    # Filtra por módulo
    if modulo:
        valores = valores.filter(modulo__nombre__icontains=modulo)
        
    # Filtra por usuario
    if usuario:
        valores = valores.filter(usuario__username__icontains=usuario)
        
    # Filtra por fecha especifica
    if fecha:
        valores = valores.filter(fecha__date=fecha)

    paginator = Paginator(valores, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'valores_criticos_pres.html', {'valores': page_obj})

def modulos_registrados(request):
    """Devuelve todos los modulos registrados en la entidad 'Modulo'."""
    datos = Modulo.objects.all() 
    return render(request, 'modulos_registrados.html', {'datos': datos})
