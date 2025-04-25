from rest_framework import serializers
from .models import *

#Arquivo responsável por converter Objetos<>Json para retorno dos endpoints

class AcademiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Academia
        fields = '__all__'

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'

class TreinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treino
        fields = '__all__'

class ExercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercicio
        fields = '__all__'

class ExercicioTreinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExercicioTreino
        fields = '__all__'
