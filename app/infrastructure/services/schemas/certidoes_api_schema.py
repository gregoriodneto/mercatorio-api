from pydantic import BaseModel
from typing import List

class CertidaoAPIItem(BaseModel):
    tipo: str
    status: str
    conteudo_base64: str

class CertidaoAPIResponse(BaseModel):
    cpf_cnpj: str
    certidoes: List[CertidaoAPIItem]