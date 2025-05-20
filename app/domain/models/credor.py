from app.interfaces.schemas.credor_schema import CredorOutput
from app.interfaces.schemas.precatorio_schema import PrecatorioOutput

class Credor:
    def __init__(self, id, nome, cpf_cnpj, email, telefone, precatorio = None):
        self.id = id
        self.nome = nome
        self.cpf_cnpj = cpf_cnpj
        self.email = email
        self.telefone = telefone
        self.precatorio = precatorio

    def to_output(self) -> CredorOutput:
        return CredorOutput(
            id=self.id,
            nome=self.nome,
            cpf_cnpj=self.cpf_cnpj,
            email=self.email,
            telefone=self.telefone,
            precatorio=(
                PrecatorioOutput(
                    id=self.precatorio.id,
                    credor_id=self.precatorio.credor_id,
                    numero_precatorio=self.precatorio.numero_precatorio,
                    valor_nominal=self.precatorio.valor_nominal,
                    foro=self.precatorio.foro,
                    data_publicacao=self.precatorio.data_publicacao
                ) if self.precatorio else None
            )            
        )