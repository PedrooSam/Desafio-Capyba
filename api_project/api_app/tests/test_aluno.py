from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from ..models import Aluno, Academia

User = get_user_model()

class AlunoAPITestes(APITestCase):

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

        self.aluno_data = {
            "nome": "Gabriel Ganley",
            "email": "gabriel@academiairnoberg.com",
            "data_nascimento": "1990-01-01",
            "academia": self.academia
        }

        self.aluno = Aluno.objects.create(**self.aluno_data)

        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)

        self.url = "/api/alunos/"

    def test_create_aluno(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        self.aluno_data['email'] = 'gabrielganley@academiairnoberg.com'

        response = self.client.post(self.url, self.aluno_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["nome"], self.aluno_data["nome"])
        self.assertEqual(response.data["email"], self.aluno_data["email"])
        self.assertEqual(str(response.data["data_nascimento"]), self.aluno_data["data_nascimento"])
        self.assertEqual(response.data["academia"], self.aluno_data["academia"])

    def test_list_aluno(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        response = self.client.get(self.url, format='json')
        response_data = response.json()['results']

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_data), 1)
        self.assertEqual(response_data[0]["nome"], self.aluno_data["nome"])
        self.assertEqual(response_data["email"], self.aluno_data["email"])
        self.assertEqual(str(response_data["data_nascimento"]), self.aluno_data["data_nascimento"])
        self.assertEqual(response_data["academia"], self.aluno_data["academia"])

    def test_get_aluno_id(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        response = self.client.get(f"{self.url}{self.aluno.id}/", format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["nome"], self.aluno_data["nome"])
        self.assertEqual(response.data["email"], self.aluno_data["email"])
        self.assertEqual(str(response.data["data_nascimento"]), self.aluno_data["data_nascimento"])
        self.assertEqual(response.data["academia"], self.aluno_data["academia"])

    def test_update_aluno(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        update_data = {"nome": "Gabriel Ganley Atualizado"}

        response = self.client.put(f"{self.url}{self.aluno.id}/", update_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["nome"], update_data['nome'])
        self.assertEqual(response.data["email"], self.aluno_data["email"])
        self.assertEqual(str(response.data["data_nascimento"]), self.aluno_data["data_nascimento"])
        self.assertEqual(response.data["academia"], self.aluno_data["academia"])

    def test_delete_aluno(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        response = self.client.delete(f"{self.url}{self.aluno.id}/", format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_aluno_id_not_found(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        response = self.client.get(f"{self.url}999999/", format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_aluno_unauthorized(self):
        response = self.client.post(self.url, self.aluno_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
