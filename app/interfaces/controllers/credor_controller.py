from fastapi import APIRouter, HTTPException
from app.use_cases.cadastrar_credor import CadastrarCredor
from app.infrastructure.database.repositories.credor_repository import CredorRepository
from app.interfaces.schemas.credor_schema import CredorInput, CredorOutput

router = APIRouter()

repo = CredorRepository()
use_case = CadastrarCredor(repo)

@router.post("/credores", response_model=CredorOutput, tags=["Credores"])
def criar_credor(credor_input: CredorInput):
    credor_dict = credor_input.model_dump()
    credor = use_case.execute(credor_dict)
    return credor