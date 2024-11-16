from ..models import Registros, Modulo
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
            - Si cualquier validación falla en POST, devuelve los errores con un código de estado 400 (Bad Request).
            - Si el remitente no tiene el token valido o nulo, devuelve un mensaje y un código de estado 401 (Unauthorized)
    """
    if request.method == "GET":
        registros = Registros.objects.all().order_by("-fecha", "-hora")
        registros_serializer = RegistrosSerializer(registros, many=True)
        return Response(registros_serializer.data, status=status.HTTP_200_OK)

    elif request.method=="POST":
        token = request.headers.get("token")
        
        if not token: #Verifica que se haya pasado un token
            return Response({"error": "Token missing"}, status=status.HTTP_400_BAD_REQUEST)
        
        if token == API_SECRET_TOKEN: #Verifica que el token que se paso sea correcto
            modulo_id = request.data.get("modulo") #modulo es el id del modulo
            ubicacion_enviada = request.data.get("ubicacion")
            
            if modulo_id and ubicacion_enviada:
                if Modulo.objects.filter(id=modulo_id).exists():
                    modulo_id = Modulo.objects.get(id=modulo_id)
                    #Verifica que si el modulo cambio la ubicacion, se actualice dicho valor en el modulo
                    if modulo_id.ubicacion != ubicacion_enviada: 
                        modulo_id.ubicacion = ubicacion_enviada
                        modulo_id.save()
                    registros_serializer = RegistrosSerializer(data=request.data)
                    if registros_serializer.is_valid():
                        registros_serializer.save()
                        return Response(registros_serializer.data, status=status.HTTP_201_CREATED)
                    
                    return Response(registros_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
                return Response({"error": "Modulo not found"}, status=status.HTTP_404_NOT_FOUND)
            
            return Response({"error": "modulo o ubicacion no enviados"}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({"error": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED)
        
@api_view(['GET'])
def registros_ubicacion_view(request, ubicacion):
    """Devuelve los registros filtrados por la ubicación proporcionada."""
    registros = Registros.objects.filter(modulo__ubicacion__iexact=ubicacion)
    if registros.exists():
        registros_serializer = RegistrosSerializer(registros, many=True)
        return Response(registros_serializer.data, status=status.HTTP_200_OK)
    return Response({"message": "No se encontraron registros para esta ubicación."}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def registros_modulo_view(request, modulo):
    """Devuelve los registros filtrados por el nombre del módulo proporcionado."""
    if not Modulo.objects.filter(nombre=modulo).exists():
        return Response({"message": "Módulo no encontrado."}, status=status.HTTP_404_NOT_FOUND)
    
    registros = Registros.objects.filter(modulo__nombre=modulo)
    
    if registros.exists():
        registros_serializer = RegistrosSerializer(registros, many=True)
        return Response(registros_serializer.data, status=status.HTTP_200_OK)
    return Response({"message": "No se encontraron registros para este módulo."}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def registros_fecha_view(request, fecha_max, fecha_min):
    """Devuelve todos los registros en el intervalo entre dos fechas."""
    try:
        fecha_max = datetime.strptime(fecha_max, '%Y-%m-%d').date()
        fecha_min = datetime.strptime(fecha_min, '%Y-%m-%d').date()
        if fecha_min > fecha_max:
            return Response({"message": "El rango de fechas es inválido. 'fecha_min' debe ser menor o igual a 'fecha_max'."}, 
                            status=status.HTTP_400_BAD_REQUEST)
    except ValueError:
        return Response({"message": "Formato de fecha inválido. Use 'YYYY-MM-DD'."}, status=status.HTTP_400_BAD_REQUEST)

    registros = Registros.objects.filter(fecha__gte=fecha_min, fecha__lte=fecha_max)
    if registros.exists():
        registros_serializer = RegistrosSerializer(registros, many=True)
        return Response(registros_serializer.data, status=status.HTTP_200_OK)

    return Response({"message": "No se encontraron registros en ese intervalo de tiempo."}, status=status.HTTP_404_NOT_FOUND)