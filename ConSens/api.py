from .models import Registros
from .serializer import RegistrosSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from datetime import datetime
from Teocom.secrets import API_SECRET_TOKEN

@api_view(['GET','POST'])
def registros_api_view(request):
    """
    Maneja las operaciones GET y POST para la entidad 'Registros'.

    - Si el método HTTP es GET, devuelve todos los registros ordenados por fecha y hora.
    - Si el método HTTP es POST, valida los datos recibidos y verifica la autenticidad del remitente, si son correctos, almacena un nuevo registro.

    Args:
        request (HttpRequest): La solicitud HTTP, que puede ser de tipo GET o POST.

    Returns:
        Response: 
            - En el caso de GET, devuelve una lista de registros con un código de estado 200 (OK).
            - En el caso de POST, devuelve los datos creados con un código de estado 201 (Created) si la validación es exitosa.
            - Si la validación falla en POST, devuelve los errores con un código de estado 400 (Bad Request).
            - Si el remitente no tiene el token valido o nulo, devuelve un mensaje y un código de estado 401 (Unauthorized)
    """
    if request.method=="GET":
        registros = Registros.objects.all().order_by("fecha","hora")
        registros_serializer = RegistrosSerializer(registros, many=True)
        return Response(registros_serializer.data, status=status.HTTP_200_OK)

    elif request.method=="POST":
        token = request.headers.get("token")
        if token == API_SECRET_TOKEN:
            registros_serializer = RegistrosSerializer(data=request.data)
            if registros_serializer.is_valid(): 
                registros_serializer.save()
                return Response(registros_serializer.data, status=status.HTTP_201_CREATED)
            return Response(registros_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "Invalid or missing token"}, status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(['GET'])
def registros_ubicacion_view(request, ubicacion):
    """Devuelve los registros filtrados por ubicacion."""
    registros = Registros.objects.filter(ubicacion=ubicacion)
    if registros.exists():
        registros_serializer = RegistrosSerializer(registros, many=True)
        return Response(registros_serializer.data, status=status.HTTP_200_OK)
    return Response({"message": "No se encontraron registros para esta ubicación."}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def registros_modulo_view(request, modulo):
    """Devuelve los registros filtrados por modulo"""
    registros = Registros.objects.filter(modulo=modulo)
    if registros.exists():
        registros_serializer = RegistrosSerializer(registros, many=True)
        return Response(registros_serializer.data, status=status.HTTP_200_OK)
    return Response({"message": "No se encontraron registros para este módulo."}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def registros_fecha_view(request, fecha_max, fecha_min):
    """Devuelve todos los datos de la tabla 'Registros' registrados entre dos fechas.

    Args:
        request (HttpRequest): La solicitud HTTP GET.
        fecha_max (str): La fecha máxima en formato 'YYYY-MM-DD'.
        fecha_min (str): La fecha mínima en formato 'YYYY-MM-DD'.

    Returns:
        Response: 
            - Lista de registros si existen datos en ese intervalo, con código de estado 200 (OK).
            - Si no encuentra ningun dato que coincida con el filtrado devuelve un mensaje con un codigo 404 (Not Found)
            - Si las fechas proporcionadas no tienen un formato valido, se devuelve un mensaje con un codigo 400 (Bad Request)
    Raises:
        ValueError: Si las fechas proporcionadas no tienen el formato 'YYYY-MM-DD', se captura y devuelve un mensaje de error indicando el formato correcto.
    """
    try:
        fecha_max = datetime.strptime(fecha_max, '%Y-%m-%d').date()
        fecha_min = datetime.strptime(fecha_min, '%Y-%m-%d').date()
    except ValueError:
        return Response({"message": "Formato de fecha inválido. Use 'YYYY-MM-DD'."}, status=status.HTTP_400_BAD_REQUEST)

    registros = Registros.objects.filter(fecha__gt=fecha_min, fecha__lt=fecha_max)
    if registros.exists():
        registros_serializer = RegistrosSerializer(registros, many=True)
        return Response(registros_serializer.data, status=status.HTTP_200_OK)
    
    return Response({"message": "No se encontraron registros en ese intervalo de tiempo."}, status=status.HTTP_404_NOT_FOUND)