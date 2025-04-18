from django.db import models

# Create your models here.

class Unidade(models.Model):
    cidade = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE, related_name="professores")

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField()
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE, related_name="alunos")

class Treino(models.Model):
    nome = models.CharField(max_length=50)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name="treinos")
    professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, related_name="treinos")

class Exercicio(models.Model):
    nome = models.CharField(max_length=50)
    grupo_muscular = models.CharField(max_length=50)

class ExercicioTreino(models.Model):
    exercicio = models.ForeignKey(Exercicio, on_delete=models.CASCADE)
    treino = models.ForeignKey(Treino, on_delete=models.CASCADE)
    descricao = models.TextField()
    ordem = models.PositiveIntegerField()
    series = models.PositiveIntegerField()
    repeticoes = models.PositiveIntegerField()