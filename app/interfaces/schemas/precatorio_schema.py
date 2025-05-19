from pydantic import BaseModel
from datetime import date

class PrecatorioInput(BaseModel):
    credor_id: int
    numero_precatorio: str
    valor_nominal: float
    foro: str
    data_publicacao: date

class PrecatorioOutput(BaseModel):
    id: int
    credor_id: int
    numero_precatorio: str
    valor_nominal: float
    foro: str
    data_publicacao: date

    class Config:
        orm_mode = True