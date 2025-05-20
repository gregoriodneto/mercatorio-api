from pydantic import BaseModel
from datetime import datetime
from fastapi import Form

class DocumentoInput(BaseModel):
    tipo: str
    
    @classmethod
    def as_form(
        cls,
        tipo: str = Form(...)
    ):
        return cls(tipo=tipo)

class DocumentoOutput(BaseModel):
    id: int
    credor_id: int
    tipo: str
    arquivo_url: str
    enviado_em: datetime

    class Config:
        model_config = {
            "from_attributes": True
        }