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
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres123
POSTGRES_DB=mercatorio
DATABASE_URL=postgresql://postgres:postgres123@localhost:5432/mercatorio

API_MOCK_CERTIDOES=http://127.0.0.1:8001/api/certidoes

DAYS_UPDATE_CERTIDAO_JOB=30
SCHEDULE_RUN_TRIGGER_INTERVAL_HOURS=24
```

3. Instale as dependências (Para utilizar local):
```bash
pip install -r requirements.txt
```

4. Rode a API principal (Para utilizar local):
```bash
uvicorn main:app --reload --port 8000
```
Acesseo o Swagger:
➡️ http://localhost:8000/docs

5. Rode a API de mock de certidões (Para utilizar local):
```bash
uvicorn app.infrastructure.services.certidao_api_mock:app --reload --port 8001
```
Acesse o Swagger:
➡️ http://localhost:8001/docs


## ✅ Observação:
Na rota ```POST /credores/:id/certidoes``` no ```Swagger``` para enviar o arquivo será desta forma:
```bash
curl -X POST "http://127.0.0.1:8000/credores/2/certidoes" \
  -F "origem=manual" \
  -F "tipo=negativa" \
  -F "status=pendente" \
  -F "file=@/caminho/arquivo.png"
```
Por que no Swagger como nesta parte não é obrigatório o File devido a regra de negócios
Que ele pode buscar com base na origem sendo ```api``` em vez de ```manual```, então 
não irá permitir seleciar um arquivo ```Swagger```.

Para rodar com Docker, basta utilizar:
```bash
docker-compose up --build
```

## 📂 Endpoints principais
- ```POST /credores```: Cadastra credor e precatório
- ```POST /credores/:id/documentos```: Upload de documentos
- ```POST /credores/:id/certidoes```: Upload manual de certidões
- ```POST /credores/:id/buscar-certidoes```: Obtenção via API mock
- ```GET /credores/:id```: Consulta geral do credor
- ```GET /api/certidoes?cpf_cnpj=00000000000```: API mock de certidões (query param cpf_cnpj)