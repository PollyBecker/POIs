from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import POI

class POITestCase(APITestCase):
    def setUp(self):
        # Configuração inicial para os testes
        self.poi_data = {
            "x": 10,
            "y": 20,
            "name": "Test POI",
            "description": "Teste das POIs"
        }
        self.poi = POI.objects.create(**self.poi_data)
        self.poi_list_url = reverse('poi-list')
        self.poi_proximity_url = reverse('poi-proximity')

    def test_create_poi(self):
        # Teste para criar um novo POI
        data = {
            "x": 30,
            "y": 40,
            "name": "Nova POI",
            "description": "Teste criar POI"
        }
        response = self.client.post(self.poi_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['poi']['name'], data['name'])

    def test_create_duplicate_poi(self):
        # Teste para tentar criar um POI duplicado
        response = self.client.post(self.poi_list_url, self.poi_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['message'], "Ops! Localização já foi cadastrada na terra média!")

    def test_poi_proximity(self):
        # Teste para verificar a proximidade dos POIs
        data = {
            "x": 10,
            "y": 20,
            "max_distance": 10
        }
        response = self.client.post(self.poi_proximity_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], self.poi_data['name'])

    def test_poi_proximity_no_results(self):
        # Teste para verificar a proximidade dos POIs sem resultados
        data = {
            "x": 100,
            "y": 200,
            "max_distance": 10
        }
        response = self.client.post(self.poi_proximity_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
