# Concessionária API

API REST desenvolvida em Django para gerenciar o estoque de veículos de uma concessionária. O sistema permite consultar carros cadastrados e verificar sua situação atual, podendo estar disponíveis, reservados ou vendidos.

## Tecnologias utilizadas

* Python
* Django
* Django REST Framework
* PostgreSQL
* Docker
* Docker Compose

## Configuração

Antes de iniciar o projeto, crie um arquivo `.env` na raiz com as seguintes variáveis:

```env
DJANGO_SECRET_KEY=chave-secreta
ALLOWED_HOSTS=*

POSTGRES_HOST=postgres
POSTGRES_PORT=5432
POSTGRES_DB=nome_do_banco
POSTGRES_USER=usuario
POSTGRES_PASSWORD=senha

DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=senha-do-admin
```

O valor de `POSTGRES_HOST` deve ser `postgres`, pois esse é o nome do serviço configurado no Docker Compose.

## Como executar

Para iniciar a aplicação, execute:

```bash
docker compose up -d
```

Ao iniciar, o Docker irá:

* Criar o container do PostgreSQL;
* Aguardar o banco ficar disponível;
* Executar as migrations;
* Criar o superusuário automaticamente;
* Iniciar o servidor Django.

Após a inicialização, a API estará disponível em:

```text
http://localhost:8000
```

## Endpoints

| Método | Endpoint                   | Descrição                            |
| ------ | -------------------------- | ------------------------------------ |
| GET    | `/api/carros/`             | Lista todos os veículos              |
| GET    | `/api/carros/disponiveis/` | Lista apenas os veículos disponíveis |
| GET    | `/api/carros/reservados/`  | Lista apenas os veículos reservados  |
| GET    | `/api/carros/vendidos/`    | Lista apenas os veículos vendidos    |

## Painel administrativo

O Django Admin pode ser acessado em:

```text
http://localhost:8000/admin/
```

Utilize as credenciais definidas no arquivo `.env`.

## Logs

Para acompanhar os logs da aplicação:

```bash
docker compose logs -f
```

## Encerrando a aplicação

Parar os containers:

```bash
docker compose down
```

Parar os containers e remover os dados armazenados no banco:

```bash
docker compose down -v
```

## Objetivo do projeto

Este projeto foi desenvolvido com o objetivo de aplicar os conceitos estudados na disciplina, incluindo criação de APIs REST, integração com banco de dados PostgreSQL, operações CRUD e utilização de Docker para containerização da aplicação.
