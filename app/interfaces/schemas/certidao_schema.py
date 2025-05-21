from pydantic import BaseModel
from datetime import datetime
from fastapi import Form
from typing import Optional

class CertidaoInput(BaseModel):
    origem: str
    tipo: Optional[str]    
    status: Optional[str]
    
    @classmethod
    def as_form(
        cls,
        origem: str = Form(...),
        tipo: Optional[str] = Form(None),        
        status: Optional[str] = Form(None),
    ):
        return cls(
            tipo=tipo,
            origem=origem,
            status=status
        )

class CertidaoOutput(BaseModel):
    id: Optional[int]
    tipo: str
    credor_id: int
    origem: str
    conteudo_base64: str
    status: str
    recebida_em: datetime

    class Config:
        model_config = {
            "from_attributes": True
        }