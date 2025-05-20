from fastapi import APIRouter, HTTPException
from app.use_cases.cadastrar_credor import CadastrarCredor
from app.use_cases.buscar_credores import BuscarCredores
from app.use_cases.buscar_credor_por_id import BuscarCredorPorId
from app.infrastructure.database.repositories.credor_repository import CredorRepository
from app.infrastructure.database.repositories.precatorio_repository import PrecatorioRepository
from app.interfaces.schemas.credor_schema import CredorInput, CredorOutput
from app.interfaces.custom.response_model import ResponseModel
from app.interfaces.custom.helpers import success_response, error_response

router = APIRouter()

repo_credor = CredorRepository()
repo_precatorio = PrecatorioRepository()
use_case = CadastrarCredor(repo_credor, repo_precatorio)
use_case_get_all = BuscarCredores(repo_credor)
use_case_get_by_id = BuscarCredorPorId(repo_credor)

@router.get("/credores", response_model=ResponseModel, tags=["Credores"])
def buscar_credores():
    try:
        credores = use_case_get_all.execute()
        return success_response(
            message="Lista de credores",
            data=[credor.to_output() for credor in credores]
        )
    except Exception as e:
        return error_response(message=str(e))
    
@router.get("/credores/{id}", response_model=ResponseModel, tags=["Credores"])
def buscar_credor_por_id(id: int):
    try:
        credor = use_case_get_by_id.execute(id)
        return success_response(
            message="Lista de credores",
            data=credor.to_output()
        )
    except Exception as e:
        return error_response(message=str(e))

@router.post("/credores", response_model=ResponseModel, tags=["Credores"])
def criar_credor(credor_input: CredorInput):
    try:
        credor = use_case.execute(credor_input)
        return success_response(message="Credor criado com sucesso",data=credor.to_output())
    except Exception as e:
        return error_response(message=str(e))
    

@router.post("/credores/{id}/documentos", response_model=ResponseModel, tags=["Credores"])
def upload_documentos_pessoais(id: int):
    try:
        credor = use_case.execute(credor_input)
        return success_response(message="Credor criado com sucesso",data=CredorOutput(**vars(credor)))
    except Exception as e:
        return error_response(message=str(e))
    
@router.post("/credores/{id}/certidoes", response_model=ResponseModel, tags=["Credores"])
def upload_manual_certidoes(id: int):
    try:
        credor = use_case.execute(id)
        return success_response(message="Credor criado com sucesso",data=CredorOutput(**vars(credor)))
    except Exception as e:
        return error_response(message=str(e))
    
@router.post("/credores/{id}/buscar-certidoes", response_model=ResponseModel, tags=["Credores"])
def simula_consulta_certidoes(id: int):
    try:
        credor = use_case.execute(id)
        return success_response(message="Credor criado com sucesso",data=CredorOutput(**vars(credor)))
    except Exception as e:
        return error_response(message=str(e))