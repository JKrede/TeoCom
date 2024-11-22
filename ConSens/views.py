from django.shortcuts import render
from .models import Registros, ValorCriticoTemperatura, ValorCriticoHumedad, ValorCriticoPresion, Modulo
from django.db.models import Max
from django.db.models.functions import TruncDate
from django.core.paginator import Paginator
from django.views.decorators.http import require_http_methods

def quienes_somos(request):
    return render(request, "quienes_somos.html")

@require_http_methods(["GET"])
def mostrar_lecturas(request):
    """Devuelve todos los datos de la entidad 'Registros'."""
    sort_by = request.GET.get('sort', 'fecha')
    datos = Registros.objects.all().order_by(sort_by)
    
    paginator = Paginator(datos, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'lecturas.html', {'datos': page_obj, 'sort': sort_by})

@require_http_methods(["GET"])
def filtrar_lecturas(request):
    """Devuelve los datos de la entidad 'Registros' filtrando por ubicación, módulo y rango de fechas."""
    ubicacion = request.GET.get('ubicacion', '').strip()
    modulo = request.GET.get('modulo', '').strip()
    fecha_max = request.GET.get('fecha_max')
    fecha_min = request.GET.get('fecha_min')

    sort_by = request.GET.get('sort', 'fecha')
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
    
    datos = datos.order_by(sort_by)
    paginator = Paginator(datos, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'lecturas.html', {'datos': page_obj, 'sort': sort_by})

@require_http_methods(["GET"])
def ultimas_lecturas(request):
    """Devuelve la última lectura de cada módulo registrado y compara los valores con los valores máximos y mínimos de temperatura, humedad y presión específicos de cada módulo."""
    
    # Último registro de cada módulo
    ultimos_registros_ids = (Registros.objects.values('modulo')
                             .annotate(ultimo_id=Max('id'))
                             .values_list('ultimo_id', flat=True))
    sort_by = request.GET.get('sort', 'fecha')
    ultimos_registros = Registros.objects.filter(id__in=ultimos_registros_ids).order_by(sort_by)
    
    # Obtener los valores críticos por módulo
    valores_criticos_temp = {critico.modulo_id: critico for critico in ValorCriticoTemperatura.objects.all()}
    valores_criticos_hum = {critico.modulo_id: critico for critico in ValorCriticoHumedad.objects.all()}
    valores_criticos_pres = {critico.modulo_id: critico for critico in ValorCriticoPresion.objects.all()}
    
    registros_con_alerta = []
    
    for registro in ultimos_registros:
        registro_data = {
            'registro': registro,
            'alerta': {
                'temp': False,
                'hum': False,
                'pres': False
            }
        }
        
        # Obtener valores críticos correspondientes al módulo del registro
        critico_temp = valores_criticos_temp.get(registro.modulo_id)
        critico_hum = valores_criticos_hum.get(registro.modulo_id)
        critico_pres = valores_criticos_pres.get(registro.modulo_id)
        
        # Comparar valores del registro con los límites críticos
        if critico_temp:
            if registro.temperatura > critico_temp.temperatura_maxima or registro.temperatura < critico_temp.temperatura_minima:
                registro_data['alerta']['temp'] = True
        
        if critico_hum:
            if registro.humedad > critico_hum.humedad_maxima or registro.humedad < critico_hum.humedad_minima:
                registro_data['alerta']['hum'] = True
        
        if critico_pres:
            if registro.presion > critico_pres.presion_maxima or registro.presion < critico_pres.presion_minima:
                registro_data['alerta']['pres'] = True
        
        registros_con_alerta.append(registro_data)
    
    return render(request, 'index.html', {'ultimos_registros': registros_con_alerta, 'sort': sort_by})

@require_http_methods(["GET"])  
def valores_criticos_temperatura(request):
    """Devuelve todos los datos de la entidad 'ValorCriticoTemperatura'."""
    sort_by = request.GET.get('sort', '-fecha')
    valores = ValorCriticoTemperatura.objects.all().order_by(sort_by)
    
    paginator = Paginator(valores, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'valores_criticos_temp.html', {'valores': page_obj, 'sort': sort_by})

@require_http_methods(["GET"])
def filtrar_temp(request):
    """Devuelve los datos de la entidad 'ValorCriticoTemperatura' filtrando por módulo, usuario y fecha."""
    modulo = request.GET.get('modulo').strip()
    usuario = request.GET.get('usuario').strip()
    fecha = request.GET.get('fecha')

    sort_by = request.GET.get('sort', '-fecha')
    valores = ValorCriticoTemperatura.objects.all()
    
    # Filtra por módulo
    if modulo:
        valores = valores.filter(modulo__nombre__icontains=modulo)
        
    # Filtra por usuario
    if usuario:
        valores = valores.filter(usuario__username__icontains=usuario)
        
    # Filtra por fecha especifica
    if fecha:
        valores = valores.filter(fecha=fecha)

    valores = valores.order_by(sort_by)
    paginator = Paginator(valores, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'valores_criticos_temp.html', {'valores': page_obj, 'sort': sort_by})

@require_http_methods(["GET"])
def valores_criticos_humedad(request):
    """Devuelve todos los datos de la entidad 'ValorCriticoHumedad'."""
    sort_by = request.GET.get('sort', '-fecha')
    valores = ValorCriticoHumedad.objects.all().order_by(sort_by)
    
    paginator = Paginator(valores, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'valores_criticos_hum.html', {'valores': page_obj, 'sort': sort_by})

@require_http_methods(["GET"])
def filtrar_hum(request):
    """Devuelve los datos de la entidad 'ValorCriticoHumedad' filtrando por módulo, usuario y fecha."""
    modulo = request.GET.get('modulo').strip()
    usuario = request.GET.get('usuario').strip()
    fecha =request.GET.get('fecha')
    
    sort_by = request.GET.get('sort', '-fecha')
    valores = ValorCriticoHumedad.objects.all()
    
    # Filtra por módulo
    if modulo:
        valores = valores.filter(modulo__nombre__icontains=modulo)
        
    # Filtra por usuario
    if usuario:
        valores = valores.filter(usuario__username__icontains=usuario)
        
    # Filtra por fecha especifica
    if fecha:
        valores = valores.filter(fecha=fecha)

    valores = valores.order_by(sort_by)
    paginator = Paginator(valores, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'valores_criticos_hum.html', {'valores': page_obj, 'sort': sort_by})

@require_http_methods(["GET"])
def valores_criticos_presion(request):
    """Devuelve todos los datos de la entidad 'ValorCriticoPresion'."""
    sort_by = request.GET.get('sort', '-fecha')
    valores = ValorCriticoPresion.objects.all().order_by(sort_by)
    
    paginator = Paginator(valores, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'valores_criticos_pres.html', {'valores': page_obj, 'sort': sort_by})

@require_http_methods(["GET"])
def filtrar_pres(request):
    """Devuelve los datos de la entidad 'ValorCriticoPresion' filtrando por módulo, usuario y fecha."""
    modulo = request.GET.get('modulo').strip()
    usuario = request.GET.get('usuario').strip()
    fecha =request.GET.get('fecha')
    
    sort_by = request.GET.get('sort', '-fecha')
    valores = ValorCriticoPresion.objects.all()
    
    # Filtra por módulo
    if modulo:
        valores = valores.filter(modulo__nombre__icontains=modulo)
        
    # Filtra por usuario
    if usuario:
        valores = valores.filter(usuario__username__icontains=usuario)
        
    # Filtra por fecha especifica
    if fecha:
        valores = valores.filter(fecha=fecha)

    valores = valores.order_by(sort_by)
    paginator = Paginator(valores, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'valores_criticos_pres.html', {'valores': page_obj, 'sort': sort_by})

@require_http_methods(["GET"])
def modulos_registrados(request):
    """Devuelve todos los modulos registrados en la entidad 'Modulo'."""
    sort_by = request.GET.get('sort', '-fecha')
    datos = Modulo.objects.all().order_by(sort_by)
    return render(request, 'modulos_registrados.html', {'datos': datos, 'sort': sort_by})
