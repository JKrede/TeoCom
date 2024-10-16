from django.urls import path
from . import api
urlpatterns = [
    path("registros/", api.registros_api_view),
    path("ubicacion/", api.registros_ubicacion_view),
    path("modulo/", api.registros_modulo_view),
]
 