from rest_framework import viewsets #Funcionalidade da DRF que já processa cada método HTTP
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

#Arquivo com a função de receber as requisições HTTP e processá-las para retornar uma resposta

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

    #Método para manipular o queryset de acordo com os parâmetros
    def get_queryset(self):
        #obterm os parâmetros da requisição
        ordenar = self.request.query_params.get('ordenar', None)
        treino_id = self.request.queryparams.get('treino_id', None)

        #Ordena os exercícios caso o parâmetro "ordenar" seja passado
        if ordenar:
            queryset = self.queryset.order_by('ordem')
        else:
            queryset = self.queryset

        #Filtra pelo parâmetro "treino_id" e o torna obrigatório, retornando um erro caso não seja passado
        if treino_id:
            queryset = queryset.filter(treino_id = treino_id)
        else:
            data = {"detail": "O parâmetro 'treino_id' é obrigatório."}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        return queryset