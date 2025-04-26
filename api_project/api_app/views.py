from rest_framework import viewsets #Funcionalidade da DRF que já processa cada método HTTP
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from drf_spectacular.utils import extend_schema

#Arquivo com a função de receber as requisições HTTP e processá-las para retornar uma resposta

@extend_schema(
    tags=["Academia"],  # Aqui você define uma tag para separar os endpoints por modelo
    summary="Gerenciar academias",
    description="Este endpoint permite criar, listar, atualizar e excluir academias."
)
class AcademiaViewSet(viewsets.ModelViewSet):
    #Puxa todos os objetos "Academia" salvos no banco
    queryset = Academia.objects.all()

    #Chama a classe serializer da model Academia
    serializer_class = AcademiaSerializer


@extend_schema(
    tags=["Professor"],  # Aqui você define uma tag para separar os endpoints por modelo
    summary="Gerenciar professores",
    description="Este endpoint permite criar, listar, atualizar e excluir professores."
)
class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


@extend_schema(
    tags=["Aluno"],  # Aqui você define uma tag para separar os endpoints por modelo
    summary="Gerenciar alunos",
    description="Este endpoint permite criar, listar, atualizar e excluir alunos."
)
class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


@extend_schema(
    tags=["Treino"],  # Aqui você define uma tag para separar os endpoints por modelo
    summary="Gerenciar treinos",
    description="Este endpoint permite criar, listar, atualizar e excluir treinos."
)
class TreinoViewSet(viewsets.ModelViewSet):
    queryset = Treino.objects.all()
    serializer_class = TreinoSerializer


@extend_schema(
    tags=["Exercicio"],  # Aqui você define uma tag para separar os endpoints por modelo
    summary="Gerenciar exercícios",
    description="Este endpoint permite criar, listar, atualizar e excluir exercícios."
)
class ExercicioViewSet(viewsets.ModelViewSet):
    queryset = Exercicio.objects.all()
    serializer_class = ExercicioSerializer


@extend_schema(
    tags=["Exercicio Treino"],  # Aqui você define uma tag para separar os endpoints por modelo
    summary="Gerenciar exercícios dos treinos",
    description="Este endpoint permite criar, listar, atualizar e excluir os exercícios dos treinos."
)
class ExercicioTreinoViewSet(viewsets.ModelViewSet):
    queryset = ExercicioTreino.objects.all()
    serializer_class = ExercicioTreinoSerializer

    #Método para manipular o queryset de acordo com os parâmetros
    def get_queryset(self):
        #obterm os parâmetros da requisição
        ordenar = self.request.query_params.get('ordenar', None)
        treino_id = self.request.query_params.get('treino_id', None)

        #Filtra pelo parâmetro "treino_id" e o torna obrigatório
        if treino_id:
            queryset = self.queryset.filter(treino_id=treino_id)
        else:
            queryset = self.queryset.none()

        #Ordena os exercícios caso o parâmetro "ordenar" seja passado
        if ordenar:
            queryset = queryset.order_by('ordem')

        return queryset