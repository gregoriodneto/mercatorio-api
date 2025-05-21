from app.interfaces.schemas.credor_schema import CredorOutput
from app.interfaces.schemas.precatorio_schema import PrecatorioOutput
from app.interfaces.schemas.documento_schema import DocumentoOutput
from app.interfaces.schemas.certidao_schema import CertidaoOutput

class Credor:
    def __init__(self, id, nome, cpf_cnpj, email, telefone, precatorio = None, documentos = None, certidoes = None):
        self.id = id
        self.nome = nome
        self.cpf_cnpj = cpf_cnpj
        self.email = email
        self.telefone = telefone
        self.precatorio = precatorio
        self.documentos = documentos
        self.certidoes = certidoes

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
            ),
            documentos=(
                (   
                    DocumentoOutput(
                        id=documento.id,
                        arquivo_url=documento.arquivo_url,
                        credor_id=documento.credor_id,
                        enviado_em=documento.enviado_em,
                        tipo=documento.tipo
                    )             
                    for documento in self.documentos
                ) if self.documentos else None
            ),
            certidoes=(
                (   
                    CertidaoOutput(
                        id=certidao.id,
                        conteudo_base64=certidao.conteudo_base64,
                        credor_id=certidao.credor_id,
                        tipo=certidao.tipo,
                        origem=certidao.origem,
                        recebida_em=certidao.recebida_em,
                        status=certidao.status,
                    )             
                    for certidao in self.certidoes
                ) if self.certidoes else None
            )          
        )