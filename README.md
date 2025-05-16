# Mercatório Backend Challenge

API REST desenvolvida com FastAPI para simular o processo de originação de precatórios. Permite o cadastro de credores, precatórios, upload de documentos e certidões, além da simulação de uma API externa para certidões.

## 🚀 Funcionalidades
- Cadastro de credores e seus precatórios
- Upload de documentos pessoais
- Upload manual de certidões
- Consulta automática de certidões via API mockada
- Consulta completa de credor (com documentos, certidões e precatórios)

## 🛠️ Tecnologias
- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker & Docker Compose
- APScheduler (para revalidação automática de certidões)

## 📦 Como executar
1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/mercatorio-api.git
cd mercatorio-api
```

2. Crie o arquivo ```.env``` (siga o .env.example):
```bash
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=
DATABASE_URL=
```

3. Suba o ambiente com Docker:
```bash
docker-compose up --build
```

4. Acesse a documentação Swagger:
```bash
http://localhost:8000/api/docs
```

## 📂 Endpoints principais
- ```POST /credores```: Cadastra credor e precatório
- ```POST /credores/:id/documentos```: Upload de documentos
- ```POST /credores/:id/certidoes```: Upload manual de certidões
- ```POST /credores/:id/buscar-certidoes```: Obtenção via API mock
- ```GET /credores/:id```: Consulta geral do credor
- ```GET /api/certidoes```: API mock de certidões (query param cpf_cnpj)