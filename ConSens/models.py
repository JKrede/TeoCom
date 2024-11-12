from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

TECNOLOGIA={ #Tipo de tecnologias que usan los modulos
    "Wifi": "Wifi industrial",
    "LoRa": "Long Range",
    }

class Modulo(models.Model):
    """Almacena los datos de los modulos"""
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now_add=True) #Fecha de registro del modulo
    ultima_modificacion = models.DateTimeField(auto_now=True) #Ultima modificacion
    nombre = models.CharField(max_length=64, null=False, unique=True) #Nombre del modulo
    grupo = models.CharField(max_length=32, null=False) #Grupo que realizo el modulo
    ubicacion = models.CharField(max_length=64, null=False) #Ubicacion del modulo
    tipo = models.CharField(max_length=16, choices=TECNOLOGIA, null=False)
     
    class Meta:
        verbose_name = "Modulo"
        verbose_name_plural = "Modulos"
        
    def __str__(self):
        return (f"Modulo: {self.nombre} creado el: {self.fecha} por: {self.grupo} ultima modificacion: {self.ultima_modificacion} en: {self.ubicacion} ")
    
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

class Registros(models.Model):
    """Almacena las mediciones de temperatura, humedad y presion por modulo y ubicacion."""
    id = models.AutoField(primary_key=True)
    fecha = models.DateField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)
    modulo = models.ForeignKey(Modulo, on_delete=models.SET_NULL, null=True) #El modulo que registro
    temperatura = models.IntegerField() #temperatura medida en grados celcius
    humedad = models.DecimalField(max_digits=5, decimal_places=2) #humedad medida en porcentaje
    presion = models.IntegerField() #presion medida en pascales
    
    class Meta:
        verbose_name = "Registro"
        verbose_name_plural = "Registros"
        
    def __str__(self):
        return (f"Modulo: {self.modulo.nombre} Dia: {self.fecha} hora: {self.hora} en: {self.modulo.ubicacion} "
            f"los datos registrados son: temperatura: {self.temperatura} [°C], "
            f"humedad: {self.humedad} [%], presion: {self.presion} [Pa]")
    
class ValorCriticoTemperatura(models.Model):
    """Almacena el historico de los valores criticos de temperatura."""
    id = models.AutoField(primary_key=True)
    fecha = models.DateField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuarios, on_delete=models.SET_NULL, null=True) #Usuario que realizo el cambio
    modulo = models.ForeignKey(Modulo, on_delete=models.SET_NULL, null=True) #El modulo donde se realizo el cambio
    temperatura_maxima = models.IntegerField() #temperatura maxima en grados celcius
    temperatura_minima = models.IntegerField() #temperatura minima en grados celcius
    
    class Meta:
        verbose_name = "Valor critico de temperatura"
        verbose_name_plural = "Valores criticos de temperatura"
        
    def temp_validation(self):
        """Validación para asegurar que la temperatura máxima sea mayor que la mínima."""
        if self.temperatura_maxima is not None and self.temperatura_minima is not None:
            if self.temperatura_maxima <= self.temperatura_minima:
                raise ValidationError("La temperatura máxima debe ser mayor que la temperatura mínima.")
            
    def save(self, *args, **kwargs):
        """Sobrescritura del metodo save: Para si no se especifica un valor de temperatura minimo o maximo tome el valor del registro anterior."""
        self.temp_validation()
        if not self.pk:
            ultimo_registro = ValorCriticoTemperatura.objects.order_by('-fecha', '-hora').first()
            
            if ultimo_registro:

                if self.temperatura_maxima is None:
                    self.temperatura_maxima = ultimo_registro.temperatura_maxima

                if self.temperatura_minima is None:
                    self.temperatura_minima = ultimo_registro.temperatura_minima
            else:
                self.temperatura_maxima = 999
                self.temperatura_minima = -200
                
        super().save(*args, **kwargs)
        
    def __str__(self):
        return "Valor critico maximo: %s[°C], Valor critico minimo: %s[°C] seteado: %s a las %s"\
        %(self.temperatura_maxima, self.temperatura_minima, self.fecha, self.hora)
        
class ValorCriticoHumedad(models.Model):
    """Almacena el historico de los valores criticos de humedad."""
    id = models.AutoField(primary_key=True)
    fecha = models.DateField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuarios, on_delete=models.SET_NULL, null=True) #Usuario que realizo el cambio
    modulo = models.ForeignKey(Modulo, on_delete=models.SET_NULL, null=True) #El modulo donde se realizo el cambio
    humedad_maxima = models.DecimalField(max_digits=5, decimal_places=2) #humedad maxima medida en porcentaje
    humedad_minima = models.DecimalField(max_digits=5, decimal_places=2) #humedad minima medida en porcentaje
    
    class Meta:
        verbose_name = "Valor critico de humedad"
        verbose_name_plural = "Valores criticos de humedad"
     
    def hum_validation(self):
        """Validación para asegurar que la humedad máxima sea mayor que la mínima."""
        if self.humedad_maxima is not None and self.humedad_minima is not None:
            if self.humedad_maxima <= self.humedad_minima:
                raise ValidationError("La humedad máxima debe ser mayor que la humedad mínima.")
            
    def save(self, *args, **kwargs):
        """Sobrescritura del metodo save: Para si no se especifica un valor de humedad minimo o maximo tome el valor del registro anterior."""
        self.hum_validation()
        if not self.pk:
            ultimo_registro = ValorCriticoHumedad.objects.order_by('-fecha', '-hora').first()
            
            if ultimo_registro:

                if self.humedad_maxima is None:
                    self.humedad_maxima = ultimo_registro.humedad_maxima

                if self.humedad_minima is None:
                    self.humedad_minima = ultimo_registro.humedad_minima
            else:
                self.humedad_maxima = 99.99
                self.humedad_minima = 0.00
                
        super().save(*args, **kwargs)
           
    def __str__(self):
        return "Valor critico maximo: %s[%], Valor critico minimo: %s[%] seteado: %s a las %s"\
        %(self.temperatura_maxima, self.temperatura_minima, self.fecha, self.hora)
        
class ValorCriticoPresion(models.Model):
    """Almacena el historico de los valores criticos de presion."""
    id = models.AutoField(primary_key=True)
    fecha = models.DateField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuarios, on_delete=models.SET_NULL, null=True) #Usuario que realizo el cambio
    modulo = models.ForeignKey(Modulo, on_delete=models.SET_NULL, null=True) #El modulo donde se realizo el cambio
    presion_maxima = models.IntegerField() #presion maxima en pascales
    presion_minima = models.IntegerField() #presion minima en pascales
    
    class Meta:
        verbose_name = "Valor critico de presion"
        verbose_name_plural = "Valores criticos de presion"
    
    def pres_validation(self):
        """Validación para asegurar que la presion máxima sea mayor que la mínima."""
        if self.presion_maxima is not None and self.presion_minima is not None:
            if self.presion_maxima <= self.presion_minima:
                raise ValidationError("La presion máxima debe ser mayor que la presion mínima.")
            
    def save(self, *args, **kwargs):
        """Sobrescritura del metodo save: Para si no se especifica un valor de presion minimo o maximo tome el valor del registro anterior."""
        self.pres_validation()
        if not self.pk:
            ultimo_registro = ValorCriticoPresion.objects.order_by('-fecha', '-hora').first()
            
            if ultimo_registro:

                if self.presion_maxima is None:
                    self.presion_maxima = ultimo_registro.presion_maxima

                if self.presion_minima is None:
                    self.presion_minima = ultimo_registro.presion_minima
            else:
                self.presion_maxima = 999999
                self.presion_minima = 0
                
        super().save(*args, **kwargs)
        
    def __str__(self):
        return "Valor critico maximo: %s[Pa], Valor critico minimo: %s[Pa] seteado: %s a las %s"\
        %(self.temperatura_maxima, self.temperatura_minima, self.fecha, self.hora)
