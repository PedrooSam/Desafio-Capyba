from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from ..models import Professor, Academia

User = get_user_model()

class ProfessorAPITestes(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="usuario", email="usuario@email.com", password="senha123")

        academia_data = {
            "nome": "Iron Berg",
            "cidade": "Recife",
            "bairro": "Boa Viagem",
            "rua": "Rua das Palmeiras",
            "numero": "1200",
            "telefone": "(81) 99888-7766",
            "email": "contato@academiaironberg.com"
        }

        self.academia = Academia.objects.create(**academia_data)

        self.professor_data = {
            "nome": "Renato Cariani",
            "cpf": "12345678901",
            "email": "renatocariani@academiaironberg.com",
            "telefone": "(81) 99888-7766",
            "academia": self.academia
        }

        self.professor = Professor.objects.create(**self.professor_data)

        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)

        self.url = "/api/professores/"

    def test_create_professor(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        response = self.client.post(self.url, self.professor_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["nome"], self.professor_data["nome"])

    def test_list_professor(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        response = self.client.get(self.url, format='json')
        response_data = response.json()['results']

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_data), 1)
        self.assertEqual(response_data[0]["nome"], self.professor_data["nome"])
        self.assertEqual(response_data[0]["cpf"], self.professor_data["cpf"])
        self.assertEqual(response_data[0]["email"], self.professor_data["email"])
        self.assertEqual(response_data[0]["telefone"], self.professor_data["telefone"])
        self.assertEqual(response_data[0]["academia"], self.professor_data["academia"])

    def test_get_professor_id(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        response = self.client.get(f"{self.url}{self.professor.id}/", format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["nome"], self.professor_data["nome"])
        self.assertEqual(response.data["cpf"], self.professor_data["cpf"])
        self.assertEqual(response.data["email"], self.professor_data["email"])
        self.assertEqual(response.data["telefone"], self.professor_data["telefone"])
        self.assertEqual(response.data["academia"], self.professor_data["academia"])

    def test_update_professor(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        update_data = {"nome": "Renato Cariani Atualizado",}

        response = self.client.put(f"{self.url}{self.professor.id}/", update_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["nome"], update_data['nome'])
        self.assertEqual(response.data["cpf"], self.professor_data["cpf"])
        self.assertEqual(response.data["email"], self.professor_data["email"])
        self.assertEqual(response.data["telefone"], self.professor_data["telefone"])
        self.assertEqual(response.data["academia"], self.professor_data["academia"])

    def test_delete_professor(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        response = self.client.delete(f"{self.url}{self.professor.id}/", format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_professor_id_not_found(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        response = self.client.get(f"{self.url}999999/", format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_professor_unauthorized(self):
        response = self.client.post(self.url, self.professor_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)