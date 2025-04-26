from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from ..models import *

User = get_user_model()

class AcademiaAPITestes(APITestCase):

    #Método chamado antes da execução de cada teste, para configurações iniciais
    def setUp(self):
        #Cria um usuário para fazer os testes
        self.user = User.objects.create_user(username="usuario", email="usuario@email.com", password="senha123")

        self.academia_data = {
            "nome": "Iron Berg",
            "cidade": "Recife",
            "bairro": "Boa Viagem",
            "rua": "Rua das Palmeiras",
            "numero": "1200",
            "telefone": "(81) 99888-7766",
            "email": "contato@academiaironberg.com"
        }

        #Adiciona uma academia ao banco para os testes
        self.academia = Academia.objects.create(**self.academia_data)

        #Salva o token jwt para autenticação do usuário nos testes
        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)

        #Salva o endpoint de academias
        self.url = "/api/academias/"


    #Teste de criação de uma instancia de Academia
    def test_create_academia(self):
        #Adiciona o token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        self.academia_data['email'] = "email@academiaironberg.com"

        #Faz a requisição
        response = self.client.post(self.url, self.academia_data, format='json')

        #Verifica se as informações estão corretas
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(response.data["nome"], self.academia_data["nome"])
        self.assertEqual(response.data["cidade"], self.academia_data["cidade"])
        self.assertEqual(response.data["bairro"], self.academia_data["bairro"])
        self.assertEqual(response.data["rua"], self.academia_data["rua"])
        self.assertEqual(response.data["numero"], self.academia_data["numero"])
        self.assertEqual(response.data["telefone"], self.academia_data["telefone"])
        self.assertEqual(response.data["email"], self.academia_data["email"])


    #Teste de leitura de todos os objetos Academia
    def test_list_academia(self):
        #Adiciona o token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        response = self.client.get(self.url, format='json')
        response_data = response.json()['results']

        #Verifica se as informações estão corretas
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        self.assertEqual(response_data[0]["nome"], self.academia_data["nome"])
        self.assertEqual(response_data[0]["cidade"], self.academia_data["cidade"])
        self.assertEqual(response_data[0]["bairro"], self.academia_data["bairro"])
        self.assertEqual(response_data[0]["rua"], self.academia_data["rua"])
        self.assertEqual(response_data[0]["numero"], self.academia_data["numero"])
        self.assertEqual(response_data[0]["telefone"], self.academia_data["telefone"])
        self.assertEqual(response.data[0]["email"], self.academia_data["email"])


    def test_get_academia_id(self):
        #Adiciona o token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        
        response = self.client.get(f"{self.url}{self.academia.id}/", format='json')
        
        #Verifica o status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        #Verifica se as informações estão corretas
        self.assertEqual(response.data["nome"], self.academia_data["nome"])
        self.assertEqual(response.data["cidade"], self.academia_data["cidade"])
        self.assertEqual(response.data["bairro"], self.academia_data["bairro"])
        self.assertEqual(response.data["rua"], self.academia_data["rua"])
        self.assertEqual(response.data["numero"], self.academia_data["numero"])
        self.assertEqual(response.data["telefone"], self.academia_data["telefone"])
        self.assertEqual(response.data["email"], self.academia_data["email"])


    def update_academia(self):
        #Adiciona o token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        update_data = {"nome": "Iron Berg 2"}

        #Faz a requisição
        response = self.client.put(f"{self.url}{self.academia.id}/", update_data, format='json')

        #Verifica se as informações estão corretas
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["nome"], update_data['nome'])


    def test_delete_academia(self):
        #Adiciona o token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        
        #Faz a requisição
        response = self.client.delete(f"{self.url}{self.academia.id}/", format='json')

        #Verifica o status code
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


    def test_get_academia_id_not_found(self):
        #Adiciona o token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        # Tentar buscar uma academia com um ID que não existe
        response = self.client.get(f"{self.url}999999/", format='json')
        
        #Verifica o status code
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_create_academia_unauthorized(self):
        #Faz a requisição sem o token jwt
        response = self.client.post(self.url, self.academia_data, format='json')
        
        #Verifica o status code
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)