from django.db import models
from django.contrib.auth.models import AbstractUser


class Registros(models.Model):
    """Almacena las mediciones de temperatura, humedad y presion por modulo y ubicacion."""
    id = models.AutoField(primary_key=True)
    fecha = models.DateField('Fecha',auto_now_add=True)
    hora = models.TimeField('Hora',auto_now_add=True)
    modulo = models.CharField('Nombre del modulo',max_length=64, null=False) #Nombre del modulo
    ubicacion = models.CharField('ubicacion',max_length=64, null=False) #Ubicacion del modulo
    temperatura = models.IntegerField('Temperatura registrada') #temperatura medida en grados celcius
    humedad = models.DecimalField('Humedad registrada',max_digits=5, decimal_places=2) #humedad medida en porcentaje
    presion = models.IntegerField('Presion registrada') #presion medida en pascales
    
    class Meta:
        verbose_name = "Registro"
        verbose_name_plural = "Registros"
        
    def __str__(self):
        return (f"Modulo: {self.modulo} Dia: {self.fecha} hora: {self.hora} en: {self.ubicacion} "
            f"los datos registrados son: temperatura: {self.temperatura} [°C], "
            f"humedad: {self.humedad} [%], presion: {self.presion} [Pa]")

class Usuarios(AbstractUser):
    """Almacena los usuarios registrados en la pagina web."""
    es_administrador = models.BooleanField(default=False)  # Este atributo indica si el usuario puede realizar cambios en valores criticos
    email = models.EmailField(unique=True)
    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        
    def __str__(self):
        return self.username
    #Los campos username esta definido en AbstractUser y password esta definido en AbstractBaseUser
    
class ValorCriticoTemperatura(models.Model):
    """Almacena el historico de los valores criticos de temperatura."""
    id = models.AutoField(primary_key=True)
    fecha = models.DateField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE) #Usuario que realizo el cambio
    modulo = models.CharField(max_length=64, default="-") #El modulo donde se realizo el cambio
    temperatura_maxima = models.IntegerField() #temperatura maxima en grados celcius
    temperatura_minima = models.IntegerField() #temperatura minima en grados celcius

    class Meta:
        verbose_name = "Valor critico de temperatura"
        verbose_name_plural = "Valores criticos de temperatura"
        
    def __str__(self):
        return "Valor critico maximo: %s[°C], Valor critico minimo: %s[°C] seteado: %s a las %s"\
        %(self.temperatura_maxima, self.temperatura_minima, self.fecha, self.hora)
        
class ValorCriticoHumedad(models.Model):
    """Almacena el historico de los valores criticos de humedad."""
    id = models.AutoField(primary_key=True)
    fecha = models.DateField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE) #Usuario que realizo el cambio
    modulo = models.CharField(max_length=64, default="-") #El modulo donde se realizo el cambio
    humedad_maxima = models.DecimalField(max_digits=5, decimal_places=2) #humedad maxima medida en porcentaje
    humedad_minima = models.DecimalField(max_digits=5, decimal_places=2) #humedad minima medida en porcentaje
    
    class Meta:
        verbose_name = "Valor critico de humedad"
        verbose_name_plural = "Valores criticos de humedad"
        
    def __str__(self):
        return "Valor critico maximo: %s[%], Valor critico minimo: %s[%] seteado: %s a las %s"\
        %(self.temperatura_maxima, self.temperatura_minima, self.fecha, self.hora)
        
class ValorCriticoPresion(models.Model):
    """Almacena el historico de los valores criticos de presion."""
    id = models.AutoField(primary_key=True)
    fecha = models.DateField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE) #Usuario que realizo el cambio
    modulo = models.CharField(max_length=64, default="-") #El modulo donde se realizo el cambio
    presion_maxima = models.IntegerField() #presion maxima en pascales
    presion_minima = models.IntegerField() #presion minima en pascales
    
    class Meta:
        verbose_name = "Valor critico de presion"
        verbose_name_plural = "Valores criticos de presion"
        
    def __str__(self):
        return "Valor critico maximo: %s[Pa], Valor critico minimo: %s[Pa] seteado: %s a las %s"\
        %(self.temperatura_maxima, self.temperatura_minima, self.fecha, self.hora)
