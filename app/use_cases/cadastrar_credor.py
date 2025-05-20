from fastapi import HTTPException
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

            prec_salvo = Precatorio(
                id=None,
                credor_id=credor.id,
                numero_precatorio=data.precatorio.numero_precatorio,
                valor_nominal=data.precatorio.valor_nominal,
                foro=data.precatorio.foro,
                data_publicacao=data.precatorio.data_publicacao,
            )
            prec_salvo = self.precatorio_repository.adicionar(prec_salvo)
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Erro ao cadastrar um credor: {str(e)}"
            )
        
        credor.precatorio = prec_salvo

        return credor.to_output()
        