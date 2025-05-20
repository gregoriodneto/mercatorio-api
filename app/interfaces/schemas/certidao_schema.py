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
        tipo: str = Form(...),        
        status: str = Form(...),
    ):
        return cls(
            tipo=tipo,
            origem=origem,
            status=status
        )

class CertidaoOutput(BaseModel):
    id: int
    tipo: str
    credor_id: int
    origem: str
    conteudo_base64: str
    status: str
    ecebida_em: datetime

    class Config:
        model_config = {
            "from_attributes": True
        }