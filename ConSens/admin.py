from django.contrib import admin
from .models import Registros, Usuarios, Modulo, ValorCriticoHumedad, ValorCriticoPresion, ValorCriticoTemperatura

admin.site.register(Registros)
admin.site.register(Usuarios)
admin.site.register(Modulo)
admin.site.register(ValorCriticoHumedad)
admin.site.register(ValorCriticoPresion)
admin.site.register(ValorCriticoTemperatura)
