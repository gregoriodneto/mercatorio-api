from app.interfaces.schemas.credor_schema import CredorOutput
from app.interfaces.schemas.precatorio_schema import PrecatorioOutput

class Credor:
    def __init__(self, id, nome, cpf_cnpj, email, telefone, precatorios = []):
        self.id = id
        self.nome = nome
        self.cpf_cnpj = cpf_cnpj
        self.email = email
        self.telefone = telefone
        self.precatorios = precatorios

    def to_output(self) -> CredorOutput:
        return CredorOutput(
            id=self.id,
            nome=self.nome,
            cpf_cnpj=self.cpf_cnpj,
            email=self.email,
            telefone=self.telefone,
            precatorios=[
                PrecatorioOutput(
                    id=p.id,
                    credor_id=p.credor_id,
                    numero_precatorio=p.numero_precatorio,
                    valor_nominal=p.valor_nominal,
                    foro=p.foro,
                    data_publicacao=p.data_publicacao
                )
                for p in self.precatorios
            ]
        )