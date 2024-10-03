from django.db import models

#Registro de datos sensados
class Registros(models.Model):
    id=models.AutoField(primary_key=True)
    fecha=models.DateTimeField(auto_now_add=True)
    hora=models.TimeField(auto_now_add=True)
    ubicacion=models.CharField(max_length=30) #Ubicacion del sensor
    temperatura=models.IntegerField() #temperatura medida en grados celcius
    humedad=models.DecimalField(max_digits=2, decimal_places=2) #humedad medida en porcentaje
    presion=models.IntegerField() #presion medida en pascales
    
    def _str_(self):
        return "Dia: %s hora: %s en: %s los datos registrados son: temperatura: %s°C, humedad: %s%, presion: %sPa"\
        %(self.fecha, self.hora, self.ubicacion, self.temperatura, self.humedad, self.presion)

#Registro de usuarios
class Usuarios(models.Model):
    id=models.AutoField(primary_key=True)
    usuario=models.CharField(max_length=30, unique=True)
    clave=models.CharField(max_length=20)
    email=models.EmailField(unique=True)
    administrador=models.BooleanField(default=False) #True: Tiene permiso para editar los valores criticos | False= no tiene permiso para editar los valores criticos
    
#Registro de cambios de los valores criticos: Temperatura
class ValorCriticoTemperatura(models.Model):
    fecha=models.DateTimeField(auto_now_add=True)
    hora=models.TimeField(auto_now_add=True)
    usuario=models.CharField(max_length=30) #Usuario que realizo el cambio
    temperatura_maxima=models.IntegerField() #temperatura maxima en grados celcius
    temperatura_minima=models.IntegerField() #temperatura minima en grados celcius

#Registro de cambios de los valores criticos: Humedad
class ValorCriticoHumedad(models.Model):
    fecha=models.DateTimeField(auto_now_add=True)
    hora=models.TimeField(auto_now_add=True)
    usuario=models.CharField(max_length=30) #Usuario que realizo el cambio
    humedad_maxima=models.IntegerField() #humedad maxima medida en porcentaje
    humedad_minima=models.IntegerField() #humedad minima medida en porcentaje

#Registro de cambios de los valores criticos: Presion
class ValorCriticoPresion(models.Model):
    fecha=models.DateTimeField(auto_now_add=True)
    hora=models.TimeField(auto_now_add=True)
    usuario=models.CharField(max_length=30) #Usuario que realizo el cambio
    presion_maxima=models.IntegerField() #presion maxima en pascales
    presion_minima=models.IntegerField() #presion minima en pascales
    
