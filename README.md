# Concessionária — API de Gerenciamento de Estoque

API REST para controle do estoque de veículos de uma concessionária, construída com Django e banco de dados PostgreSQL. Permite consultar carros por situação: disponível, reservado ou vendido.

---

## Tecnologias

- Python / Django
- PostgreSQL
- Docker + Docker Compose

---

## Variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com o conteúdo abaixo:

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

> O valor de `POSTGRES_HOST` deve ser `postgres`, que é o nome do serviço definido no Docker Compose.

---

## Como executar

```bash
docker compose up -d
```

Na inicialização, o Docker realiza automaticamente:

1. Sobe o container do PostgreSQL
2. Aguarda o banco ficar disponível (healthcheck)
3. Aplica as migrations
4. Cria o superusuário com as credenciais do `.env`
5. Sobe o servidor na porta `8000`

Para acompanhar os logs em tempo real:

```bash
docker compose logs -f
```

---

## Endpoints

Base URL: `http://localhost:8000`

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/api/carros/` | Retorna todos os veículos |
| GET | `/api/carros/disponiveis` | Veículos disponíveis para venda |
| GET | `/api/carros/reservados` | Veículos com reserva ativa |
| GET | `/api/carros/vendidos` | Veículos já vendidos |

---

## Administração

O painel administrativo está disponível em `http://localhost:8000/admin/`.

Use as credenciais configuradas nas variáveis `DJANGO_SUPERUSER_*` do `.env`.

---

## Encerrando

```bash
# Parar os containers
docker compose down

# Parar e apagar os dados do banco
docker compose down -v
```
