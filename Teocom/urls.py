"""
URL configuration for Teocom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from ConSens import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registros/', include('ConSens.urls')),
    path('', views.inicio),
    path('registrarse/', views.registrarse),
    path('quienes_somos/', views.quienes_somos),
    path('lecturas/', views.mostrar_lecturas),
    path('filtrar_lecturas/', views.filtrar_lecturas, name='filtrar_lecturas'),
    path('valores_criticos/', views.valores_criticos_temperatura), ##Por defecto muestra el de temperatura
    path('valores_criticos_temp/', views.valores_criticos_temperatura),
    path('filtrar_temp/', views.filtrar_temp, name='filtrar_temp'),
    path('valores_criticos_hum/', views.valores_criticos_humedad),
    path('filtrar_hum/', views.filtrar_hum, name='filtrar_hum'),
    path('valores_criticos_pres/', views.valores_criticos_presion),
    path('filtrar_pres/', views.filtrar_pres, name='filtrar_pres'),
]
