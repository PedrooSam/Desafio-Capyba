# **Gym Master**

O Gym Master é um sistema de gerenciamento focado em redes de academias (como por exemplo a SmartFit). O sistema permite o cadastro e manipulação da informação de diversas unidades de academias, além de alunos e professores. No mais, o sistema também possui um registro de exercícios e dos treinos dos alunos, que podem ser gerenciados pelos professores.

## 🧩 **Funcionalidades Implementadas**

- **Gestão de Academias**:
  - Criar, listar, atualizar e excluir academias.
  - A cada academia cadastrada, os dados como **nome**, **endereço**, **telefone** e **email** são registrados.

- **Gestão de Professores**:
  - Criar, listar, atualizar e excluir professores.
  - Os dados de professores incluem **nome**, **cpf**, **email**, **telefone**, e **academia** que o professor trabalha (relacionamento com a academia).

- **Gestão de Alunos**:
  - Criar, listar, atualizar e excluir alunos.
  - Informações como **nome**, **email**, **data de nascimento**, e **academia** (relacionamento com a academia) são manipuladas.

- **Gestão de Treinos**:
  - Criar, listar, atualizar e excluir treinos de um aluno.
  - Cada treino está vinculado a um aluno e a seu professor criador, com o objetivo de **controlar o plano de treinamento** do aluno.
 
- **Gestão de Exercícios**:
  - Criar, listar, atualizar e excluir exercícios.
  - A cada exercício, são registrados dados como **nome**, **grupo muscular** trabalhado no exercício.

- **Gestão de Exercícios dos treinos**:
  - Criar, listar, atualizar e excluir.
  - Manipulação dos exercícios que pertencem a cada treino.
  - A cada exercício, são registrados dados como o **exercício** registrado no treino(relacionamento com um exercício), **descrição**, **ordem**, e **treino** que ele pertence (relacionamento com um treino).
 
- **Autenticação e Permissões**:
  - Implementação de autenticação usando **JWT (JSON Web Tokens)** para garantir segurança nos endpoints.
  - Acesso aos dados é restrito a **usuários autenticados**.

- **Paginação**:
  - Implementação de paginação nos endpoints que retornam listas de objetos (como a lista de exercícios), com **10 itens por página**.
  - É possível ajustar a quantidade de itens por página usando o parâmetro de **`page_size`** na URL.
 
- **Filtro**
  - Implementação de filtro para retornar os exercícios registrados em cada treino especificamente.
 
- **Ordenação**
  - Parâmetro opcional de ordenação dos exercícios do treino pela ordem que o professor planejou para execução.

- **Testes para todos os endpoints**
  - Testes automatizados para checar a integridade do código em vários casos de uso.

- **Documentação**:
  - A documentação da API gerada usando **DRF Spectacular**, proporcionando uma interface interativa com **Swagger UI**.

  - **Como acessar a documentação**
    - /schema/ - URL para baixar a documentação
    - /docs/ - URL para acessar a documentação online


## 🚀 **Tecnologias Utilizadas**

- **Django**: Framework web de alto nível que facilita a criação de APIs seguras e rápidas na linguagem python.
- **Django REST Framework**: Extensão do Django para criar APIs RESTful, permitindo manipulação fácil de dados e autenticação.
- **DRF Spectacular**: Ferramenta para gerar automaticamente documentação para a API.
- **Djoser**: Biblioteca para implementar autenticação e registro de usuários usando JWT (JSON Web Tokens).
- **SQLite**: Banco de dados utilizado durante o desenvolvimento.
  
## ⚡ **Endpoints da API**

A API oferece diversos endpoints para gestão de academias, professores, alunos, exercícios e treinos. Aqui estão alguns exemplos:

- **Academias**:
  - `GET /api/academias/`: Lista todas as academias.
  - `GET /api/academias/{id}/`: Retorna uma academia.
  - `POST /api/academias/`: Cria uma nova academia.
  - `PUT /api/academias/{id}/`: Atualiza uma academia existente.
  - `DELETE /api/academias/{id}/`: Exclui uma academia.

- **Professores**:
  - `GET /api/professores/`: Lista todos os professores.
  - `GET /api/professores/{id}/`: Retorna um professor.
  - `POST /api/professores/`: Cria um novo professor.
  - `PUT /api/professores/{id}/`: Atualiza um professor existente.
  - `DELETE /api/professores/{id}/`: Exclui um professor.

- **Alunos**:
  - `GET /api/alunos/`: Lista todos os alunos.
  - `GET /api/alunos/{id}/`: Retorna um alunos.
  - `POST /api/alunos/`: Cria um novo aluno.
  - `PUT /api/alunos/{id}/`: Atualiza um aluno existente.
  - `DELETE /api/alunos/{id}/`: Exclui um aluno.

- **Exercícios**:
  - `GET /api/exercicios/`: Lista todos os exercícios.
  - `GET /api/exercicios/{id}/`: Retorna um exercícios.
  - `POST /api/exercicios/`: Cria um novo exercício.
  - `PUT /api/exercicios/{id}/`: Atualiza um exercício existente.
  - `DELETE /api/exercicios/{id}/`: Exclui um exercício.

- **Treinos**:
  - `GET /api/treinos/`: Lista todos os treinos.
  - `GET /api/treinos/{id}/`: Retorna um treinos.
  - `POST /api/treinos/`: Cria um novo treino.
  - `PUT /api/treinos/{id}/`: Atualiza um treino existente.
  - `DELETE /api/treinos/{id}/`: Exclui um treino.
 
- **Exercícios dos treinos**
  - `GET /api/exercicio-treino/`: Lista todos os exercícios dos treinos.
  - `POST /api/exercicio-treino/`: Cria um novo exercício dos treino.
  - `PUT /api/exercicio-treino/{id}/`: Atualiza um exercício dos treino.
  - `DELETE /api/exercicio-treino/{id}/`: Exclui um exercício dos treino.
  - O endpoint GET possui o parâmetro opcional de ordenação, que retorna os exercícios na ordem planejada pelo professor.
  - O endpoint GET também possui o parâmetro obrigatório de filtro, em que deve ser colocado o treino que se quer obter os exercícios.

- **Autenticação**:
  - `POST /auth/jwt/create/`: Cria um token JWT para autenticação.
  - `POST /auth/jwt/refresh/`: Atualiza um token JWT.

## 📝 **Como Rodar o Projeto**

### 1. **Clone o repositório**

Clone o repositório para sua máquina local:

```bash
git clone https://github.com/usuario/mini-mundo-da-academia.git
```
Crie um ambiente virtual e ative-o:
```
python3 -m venv venv
```
```
venv\Scripts\activate
```
Instale as dependências do projeto:
```
python -r requirements.txt
```
Entre na pasta do projeto:
```
cd api_project
```
Faça as migrações do banco de dados:
```
python manage.py migrate
```
Por fim, inicialize o projeto:
```
python manage.py runserver
```
