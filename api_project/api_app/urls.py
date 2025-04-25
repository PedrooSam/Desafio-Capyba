from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

#Criando router para mapear as URLs e endpoints
router = DefaultRouter()

#Chamando o método register para linkar os endpoints às views
router.register(r'academias', AcademiaViewSet)
router.register(r'professores', ProfessorViewSet)
router.register(r'alunos', AlunoViewSet)
router.register(r'treinos', TreinoViewSet)
router.register(r'exercicios', ExercicioViewSet)
router.register(r'exercicio-treinos', ExercicioTreinoViewSet)

#Registra as URLs do router
urlpatterns = [
    path('', include(router.urls)),
]