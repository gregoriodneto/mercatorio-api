from fastapi import FastAPI, Query
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.infrastructure.services.schemas.certidoes_api_schema import CertidaoAPIResponse
import os, requests, base64, json
from pathlib import Path

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

BASE_DIR = Path(__file__).resolve().parent
json_path = BASE_DIR / "certidoes_mock.json"
with open(json_path, "r") as f:
        FAKE_DB = json.load(f)

def gerar_certidao_base64(texto: str) -> str:
    return base64.b64encode(texto.encode("utf-8")).decode("utf-8")

def consultar_certidoes_externas(cpf_cnpj: str):
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
        return response.json()
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Erro na conexão com a API externa."
        )

@app.get("/api/certidoes", tags=["Certidões"])
def consultar_certidoes(cpf_cnpj: str = Query(..., min_length=11, max_length=14)) -> CertidaoAPIResponse:
    certidoes = FAKE_DB.get(cpf_cnpj)
    
    if not certidoes:
        raise HTTPException(
            status_code=404,
            detail="Certidões não encontradas para o CPF/CNPJ informado."
        )
    
    return CertidaoAPIResponse(
         cpf_cnpj=cpf_cnpj,
         certidoes=certidoes
    )