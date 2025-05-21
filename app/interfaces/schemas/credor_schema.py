from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from app.interfaces.schemas.precatorio_schema import PrecatorioOutput, PrecatorioInput
from app.interfaces.schemas.documento_schema import DocumentoOutput
from app.interfaces.schemas.certidao_schema import CertidaoOutput

class CredorInput(BaseModel):
    nome: str = Field(..., example="João da Silva")
    cpf_cnpj: str = Field(..., example="123.456.789-00")
    email: EmailStr = Field(..., example="joao@example.com")
    telefone: str = Field(..., example="(11) 99999-9999")
    precatorio: PrecatorioInput

    class Config:
        json_schema_extra = {
            "example": {
                "nome": "João da Silva",
                "cpf_cnpj": "123.456.789-00",
                "email": "joao@example.com",
                "telefone": "(11) 99999-9999",
                "precatorio": {
                        "numero_precatorio": "0001234-56.2024.8.26.0000",
                        "valor_nominal": 15000.75,
                        "foro": "São Paulo",
                        "data_publicacao": "2024-01-15"
                }                
            }
        }

class CredorOutput(BaseModel):
    id: int
    nome: str
    cpf_cnpj: str
    email: EmailStr
    telefone: str
    precatorio: Optional[PrecatorioOutput] = None
    documentos: Optional[list[DocumentoOutput]] = []
    certidoes: Optional[list[CertidaoOutput]] = []

    class Config:
        model_config = {
            "from_attributes": True
        }