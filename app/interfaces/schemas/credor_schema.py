from pydantic import BaseModel, EmailStr
from typing import List
from app.interfaces.schemas.precatorio_schema import PrecatorioOutput

class CredorInput(BaseModel):
    nome: str
    cpf_cnpj: str
    email: EmailStr
    telefone: str

class CredorOutput(BaseModel):
    id: int
    nome: str
    cpf_cnpj: str
    email: EmailStr
    telefone: str
    precatorios: List[PrecatorioOutput] = []

    class Config:
        orm_mode = True