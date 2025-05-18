from pydantic import BaseModel, EmailStr

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

    class Config:
        orm_mode = True