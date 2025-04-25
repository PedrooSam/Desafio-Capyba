from rest_framework import viewsets #Funcionalidade da DRF que já processa cada método HTTP
from .models import *
from .serializers import *

#Arquivo com a função de receber as requisições HTTP e processá-las para retornar uma resposta
'''
Métodos do ModelViewSet:

list() → responde ao GET /academias/

retrieve() → responde ao GET /academias/<id>/

create() → responde ao POST /academias/

update() → responde ao PUT /academias/<id>/

partial_update() → responde ao PATCH /academias/<id>/

destroy() → responde ao DELETE /academias/<id>/
'''

class AcademiaViewSet(viewsets.ModelViewSet):
    #Puxa todos os objetos "Academia" salvos no banco
    queryset = Academia.objects.all()

    #Chama a classe serializer da model Academia
    serializer_class = AcademiaSerializer


class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class TreinoViewSet(viewsets.ModelViewSet):
    queryset = Treino.objects.all()
    serializer_class = TreinoSerializer


class ExercicioViewSet(viewsets.ModelViewSet):
    queryset = Exercicio.objects.all()
    serializer_class = ExercicioSerializer


class ExercicioTreinoViewSet(viewsets.ModelViewSet):
    queryset = ExercicioTreino.objects.all()
    serializer_class = ExercicioTreinoSerializer
