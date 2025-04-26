from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from ..models import Treino, Aluno, Professor, Academia

User = get_user_model()

class TreinoAPITestes(APITestCase):

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

        aluno_data = {
            "nome": "Gabriel Ganley",
            "email": "gabriel@academiairnoberg.com",
            "data_nascimento": "1990-01-01",
            "academia": self.academia
        }

        professor_data = {
            "nome": "Renato Cariani",
            "cpf": "12345678901",
            "email": "renatocariani@academiaironberg.com",
            "telefone": "(81) 99888-7766",
            "academia": self.academia
        }

        self.treino_data = {
            "nome": "Treino do Arnold",
            "aluno": self.aluno,
            "professor": self.professor
        }

        self.aluno = Aluno.objects.create(**aluno_data)

        self.professor = Professor.objects.create(**professor_data)

        self.academia = Academia.objects.create(**academia_data)

        self.treino = Treino.objects.create(**self.treino_data)

        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)

        self.url = "/api/treinos/"

    def test_create_treino(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        response = self.client.post(self.url, self.treino_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["nome"], self.treino_data["nome"])

    def test_list_treino(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        response = self.client.get(self.url, format='json')
        response_data = response.json()['results']

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_data), 1)
        self.assertEqual(response_data[0]["nome"], self.treino_data["nome"])

    def test_get_treino_id(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        response = self.client.get(f"{self.url}{self.treino.id}/", format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["nome"], self.treino_data["nome"])

    def test_update_treino(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        update_data = {"nome": "Treino do Arnold Atualizado"}

        response = self.client.put(f"{self.url}{self.treino.id}/", update_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["nome"], update_data['nome'])

    def test_delete_treino(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        response = self.client.delete(f"{self.url}{self.treino.id}/", format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_treino_id_not_found(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        response = self.client.get(f"{self.url}999999/", format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_treino_unauthorized(self):
        response = self.client.post(self.url, self.treino_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)