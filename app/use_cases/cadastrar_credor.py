from fastapi import HTTPException
from app.domain.models.credor import Credor

class CadastrarCredor:
    def __init__(self, credor_repository):
        self.credor_repository = credor_repository

    def execute(self, data):
        credor_existe = self.credor_repository.obter_por_cpf_cnpj(data.cpf_cnpj)
        if credor_existe:
            raise HTTPException(
                status_code=409,
                detail="Credor com este CPF/CNPJ já existe."
            )
        credor = Credor(
            id=None,
            nome=data.nome,
            cpf_cnpj=data.cpf_cnpj,
            email=data.email,
            telefone=data.telefone
        )
        return self.credor_repository.adicionar(credor)