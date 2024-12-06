from django.test import TestCase
from django.urls import reverse
from ConSens.models import Registros, Modulo, ValorCriticoTemperatura, ValorCriticoHumedad, ValorCriticoPresion, Usuarios

class ViewsTests(TestCase):
    def setUp(self):
        # Crear datos de prueba
        self.modulo = Modulo.objects.create(
            nombre="Módulo 1",
            grupo="Grupo 1",
            ubicacion="Laboratorio",
            tipo="Wifi"
        )
        self.usuario = Usuarios.objects.create(username="test_admin", email="unit_test_admin@gmail.com", es_administrador="True")
        self.registro = Registros.objects.create(
            modulo=self.modulo,
            temperatura=25,
            humedad=50.00,
            presion=1013,
            ubicacion="Laboratorio",
        )
        self.valor_critico_temp = ValorCriticoTemperatura.objects.create(
            modulo=self.modulo,
            usuario=self.usuario,
            temperatura_minima=20,
            temperatura_maxima=30,
        )
        self.valor_critico_hum = ValorCriticoHumedad.objects.create(
            modulo=self.modulo,
            usuario=self.usuario,
            humedad_minima=40.00,
            humedad_maxima=80.00,
        )
        self.valor_critico_pres = ValorCriticoPresion.objects.create(
            modulo=self.modulo,
            usuario=self.usuario,
            presion_minima=1000,
            presion_maxima=1014,
        )
        
    def test_mostrar_lecturas_view(self):
        response = self.client.get(reverse('lecturas') + "?sort=fecha")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lecturas.html")
        self.assertContains(response, self.registro.ubicacion)

    def test_filtrar_lecturas_view(self):
        response = self.client.get(reverse('filtrar_lecturas') + "?ubicacion=Laboratorio&sort=fecha")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lecturas.html")
        self.assertContains(response, "Laboratorio")
        self.assertNotContains(response, "No Data")

    def test_ultimas_lecturas_view(self):
        response = self.client.get(reverse(''))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertContains(response, self.modulo.nombre)

    def test_valores_criticos_temperatura_view(self):
        response = self.client.get(reverse('valores_criticos_temperatura') + "?sort=-fecha")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "valores_criticos_temp.html")
        self.assertContains(response, str(self.valor_critico_temp.temperatura_minima))

    def test_filtrar_valores_criticos_temperatura_view(self):
        response = self.client.get(reverse('filtrar_valores_criticos_temperatura') + f"?modulo={self.modulo.nombre}")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "valores_criticos_temp.html")
        self.assertContains(response, str(self.valor_critico_temp.temperatura_maxima))

    def test_valores_criticos_humedad_view(self):
        response = self.client.get(reverse('valores_criticos_humedad') + "?sort=-fecha")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "valores_criticos_hum.html")

    def test_modulos_registrados_view(self):
        response = self.client.get(reverse('modulos_registrados') + "?sort=-fecha")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "modulos_registrados.html")
        self.assertContains(response, self.modulo.nombre)
