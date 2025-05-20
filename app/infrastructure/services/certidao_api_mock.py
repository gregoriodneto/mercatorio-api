from fastapi import FastAPI, Query
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os, requests, base64

app = FastAPI(
    title="API Mock - Consulta de Certidões",
    description="Mock de consulta de certidões Federais e Trabalhistas",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

def gerar_certidao_base64(texto: str) -> str:
    return base64.b64encode(texto.encode("utf-8")).decode("utf-8")

def consultar_certidoes(cpf_cnpj: str):
    URL = os.getenv('API_MOCK_CERTIDOES')
    if URL is None:
        raise HTTPException(
            status_code=500,
            detail="URL da API MOCK de Certidões não esta carregando."
        ) 
    params = { "cpf_cnpj":cpf_cnpj }

    try:
        response = requests.get(URL,params=params)
        response.raise_for_status()
        dados = response.json()
        return dados
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Erro na conexão com a API externa."
        )   


@app.get("/api/certidoes", tags=["Certidões"])
def consultar_certidoes(cpf_cnpj: str = Query(..., min_length=11, max_length=14)):
    return {
        "cpf_cnpj": cpf_cnpj,
        "certidoes": [
            {
                "tipo": "federal",
                "status": "negativa",
                "conteudo_base64": gerar_certidao_base64(f"Certidão Federal de {cpf_cnpj}")
            },
            {
                "tipo": "trabalhista",
                "status": "positiva",
                "conteudo_base64": gerar_certidao_base64(f"Certidão Trabalhista de {cpf_cnpj}")
            },
            {
                "tipo": "estadual",
                "status": "regular",
                "conteudo_base64": gerar_certidao_base64(f"Certidão Estadual de {cpf_cnpj}")
            },
            {
                "tipo": "municipal",
                "status": "isento",
                "conteudo_base64": gerar_certidao_base64(f"Certidão Municipal de {cpf_cnpj}")
            }
        ]
    }