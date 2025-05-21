from fastapi import APIRouter, File, UploadFile, Depends
from app.use_cases.cadastrar_credor import CadastrarCredor
from app.use_cases.buscar_credores import BuscarCredores
from app.use_cases.buscar_credor_por_id import BuscarCredorPorId
from app.use_cases.upload_documentos_pessoais import UploadDocumentosPessoais
from app.use_cases.upload_certidoes import UploadCertidoes
from app.infrastructure.database.repositories.credor_repository import CredorRepository
from app.infrastructure.database.repositories.precatorio_repository import PrecatorioRepository
from app.infrastructure.database.repositories.documento_repository import DocumentoRepository
from app.infrastructure.database.repositories.certidao_repository import CertidaoRepository
from app.interfaces.schemas.credor_schema import CredorInput, CredorOutput
from app.interfaces.schemas.documento_schema import DocumentoOutput, DocumentoInput
from app.interfaces.schemas.certidao_schema import CertidaoOutput, CertidaoInput
from app.interfaces.custom.response_model import ResponseModel
from app.interfaces.custom.helpers import success_response, error_response

router = APIRouter()

repo_credor = CredorRepository()
repo_precatorio = PrecatorioRepository()
repo_documento = DocumentoRepository()
repo_certidao = CertidaoRepository()

use_case = CadastrarCredor(repo_credor, repo_precatorio)
use_case_get_all = BuscarCredores(repo_credor)
use_case_get_by_id = BuscarCredorPorId(repo_credor)
use_case_upload_documento_pessoal = UploadDocumentosPessoais(repo_documento, repo_credor)
use_case_upload_certidao = UploadCertidoes(repo_certidao, repo_credor)

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
        if id is None:
            return error_response(message="Necessário enviar o id do credor.")
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
        return success_response(message="Credor criado com sucesso",data=credor)
    except Exception as e:
        return error_response(message=str(e))
    

@router.post("/credores/{id}/documentos", response_model=ResponseModel, tags=["Credores"])
async def upload_documentos_pessoais(
    id: int, 
    documento: DocumentoInput = Depends(DocumentoInput.as_form), 
    file: UploadFile = File(...)
    ):
    try:        
        if id is None:
            return error_response(message="Necessário enviar o id do credor.")     
        documento = await use_case_upload_documento_pessoal.execute(id, documento, file)
        return success_response(message="Documento Pessoal cadastrado com sucesso!",data=DocumentoOutput(**vars(documento)))
    except Exception as e:
        return error_response(message=str(e))
    
@router.post("/credores/{id}/certidoes", response_model=ResponseModel, tags=["Credores"])
async def upload_manual_certidoes(
    id: int,
    certidao: CertidaoInput = Depends(CertidaoInput.as_form), 
    file: UploadFile = File(...)
    ):
    try:
        if id is None:
            return error_response(message="Necessário enviar o id do credor.")
        certidao = await use_case_upload_certidao.execute(id, certidao, file)
        return success_response(message="Certidão vinculada ao credor",data=None)
    except Exception as e:
        return error_response(message=str(e))
    
@router.post("/credores/{id}/buscar-certidoes", response_model=ResponseModel, tags=["Credores"])
def simula_consulta_certidoes(id: int):
    try:
        credor = use_case.execute(id)
        return success_response(message="Credor criado com sucesso",data=CredorOutput(**vars(credor)))
    except Exception as e:
        return error_response(message=str(e))