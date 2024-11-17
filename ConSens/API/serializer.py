from rest_framework import serializers
from ..models import Registros, Modulo

class RegistrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registros
        fields = ['id', 'fecha', 'hora', 'modulo', 'ubicacion', 'temperatura', 'humedad', 'presion']
        read_only_fields = ['id', 'fecha', 'hora']
        
class ModuloSerializer(serializers.ModelSerializer):
    class meta:
        model = Modulo
        fields = ['id', 'fecha', 'ultima_modificacion', 'nombre', 'grupo', 'ubicacion', 'tipo']
        read_only_fields = ['id', 'fecha', 'ultima_modificacion'] 