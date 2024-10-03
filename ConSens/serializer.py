from rest_framework import serializers
from .models import Registros

class RegistrosSerializer(serializers.ModelSerializer):
    class Meta:
        model=Registros
        fields = ['id', 'fecha', 'hora', 'ubicacion', 'temperatura', 'humedad', 'presion']
        read_only_fields = ['id', 'fecha', 'hora']