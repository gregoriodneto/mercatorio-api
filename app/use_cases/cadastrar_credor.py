from fastapi import HTTPException
from app.interfaces.schemas.credor_schema import CredorOutput
from app.interfaces.schemas.precatorio_schema import PrecatorioOutput
from app.domain.models.credor import Credor
from app.domain.models.precatorio import Precatorio

class CadastrarCredor:
    def __init__(self, credor_repository, precatorio_repository):
        self.credor_repository = credor_repository
        self.precatorio_repository = precatorio_repository

    def execute(self, data):
        credor_existe = self.credor_repository.obter_por_cpf_cnpj(data.cpf_cnpj)
        if credor_existe:
            raise HTTPException(
                status_code=409,
                detail="Credor com este CPF/CNPJ já existe."
            )
        
        try:
            credor = Credor(
                id=None,
                nome=data.nome,
                cpf_cnpj=data.cpf_cnpj,
                email=data.email,
                telefone=data.telefone
            )
            credor = self.credor_repository.adicionar(credor)

            precatorios_salvos = []
            for precatorio in data.precatorios:
                prec = Precatorio(
                    id=None,
                    credor_id=credor.id,
                    numero_precatorio=precatorio.numero_precatorio,
                    valor_nominal=precatorio.valor_nominal,
                    foro=precatorio.foro,
                    data_publicacao=precatorio.data_publicacao,
                )
                prec_salvo = self.precatorio_repository.adicionar(prec)
                precatorios_salvos.append(prec_salvo)
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Erro ao cadastrar um credor: {str(e)}"
            )
        
        credor.precatorios = precatorios_salvos

        return credor.to_output()
        