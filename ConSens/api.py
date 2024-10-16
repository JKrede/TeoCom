from .models import Registros
from .serializer import RegistrosSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view



@api_view(['GET','POST'])
def registros_api_view(request):

    if request.method=="GET": #Devuelve todos los registros ordenados por fecha y hora
        registros = Registros.objects.all().order_by("fecha","hora")
        registros_serializer = RegistrosSerializer(registros, many=True)
        return Response(registros_serializer.data, status=status.HTTP_200_OK)

    elif request.method=="POST":
        registros_serializer = RegistrosSerializer(data=request.data)
        if registros_serializer.is_valid(): 
            registros_serializer.save()
            return Response(registros_serializer.data, status=status.HTTP_201_CREATED)
        return Response(registros_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def registros_ubicacion_view(request, ubicacion):
    
    registros = Registros.objects.filter(ubicacion=ubicacion)
    if registros.exists():
        registros_serializer = RegistrosSerializer(registros, many=True)
        return Response(registros_serializer.data, status=status.HTTP_200_OK)
    return Response({"message": "No se encontraron registros para esta ubicación."}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def registros_modulo_view(request, modulo):
    
    registros = Registros.objects.filter(modulo=modulo)
    if registros.exists():
        registros_serializer = RegistrosSerializer(registros, many=True)
        return Response(registros_serializer.data, status=status.HTTP_200_OK)
    return Response({"message": "No se encontraron registros para este módulo."}, status=status.HTTP_404_NOT_FOUND)
