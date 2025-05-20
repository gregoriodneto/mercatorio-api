from sqlalchemy.orm import joinedload
from app.domain.models.credor import Credor
from app.domain.models.precatorio import Precatorio
from app.domain.repositories.credor_repositoriy_interface import CredorRepositoryInterface
from app.infrastructure.database.models.credor_model import CredorModel
from app.infrastructure.database.db_config import SessionLocal

class CredorRepository(CredorRepositoryInterface):
    def __init__(self):
        self.session = SessionLocal()

    def adicionar(self, credor: Credor) -> Credor:
        db_credor = CredorModel(
            nome=credor.nome,
            cpf_cnpj=credor.cpf_cnpj,
            email=credor.email,
            telefone=credor.telefone
        )
        self.session.add(db_credor)
        self.session.commit()
        self.session.refresh(db_credor)
        credor.id = db_credor.id
        return credor

    def obter_por_id(self, credor_id: int) -> Credor:
        db_credor = self.session.query(CredorModel).options(joinedload(CredorModel.precatorio)).filter_by(id=credor_id).first()
        if db_credor is None:
            return None
        return Credor(
                id=db_credor.id,
                nome=db_credor.nome,
                cpf_cnpj=db_credor.cpf_cnpj,
                email=db_credor.email,
                telefone=db_credor.telefone,
                precatorio=
                    Precatorio(
                        id=db_credor.precatorio.id,
                        credor_id=db_credor.precatorio.credor_id,
                        numero_precatorio=db_credor.precatorio.numero_precatorio,
                        data_publicacao=db_credor.precatorio.data_publicacao,
                        foro=db_credor.precatorio.foro,
                        valor_nominal=db_credor.precatorio.valor_nominal
                    )
                
            )

    def obter_por_cpf_cnpj(self, cpf_cnpj: str) -> Credor:
        db_credor = self.session.query(CredorModel).filter_by(cpf_cnpj=cpf_cnpj).first()
        if db_credor is None:
            return None
        
        db_precatorio = db_credor.precatorio[0] if db_credor.precatorio else None

        return Credor(
            id=db_credor.id,
            nome=db_credor.nome,
            cpf_cnpj=db_credor.cpf_cnpj,
            email=db_credor.email,
            telefone=db_credor.telefone,
            precatorio=Precatorio(
                id=db_precatorio.id,
                credor_id=db_precatorio.credor_id,
                numero_precatorio=db_precatorio.numero_precatorio,
                data_publicacao=db_precatorio.data_publicacao,
                foro=db_precatorio.foro,
                valor_nominal=db_precatorio.valor_nominal
            ) if db_precatorio else None
        )

    def listar_todos(self) -> list[Credor]:
        db_credores = self.session.query(CredorModel).options(joinedload(CredorModel.precatorio)).all()
        return [
            Credor(
                id=c.id,
                nome=c.nome,
                cpf_cnpj=c.cpf_cnpj,
                email=c.email,
                telefone=c.telefone,
                precatorio=(
                    Precatorio(
                        id=c.precatorio.id,
                        credor_id=c.precatorio.credor_id,
                        numero_precatorio=c.precatorio.numero_precatorio,
                        data_publicacao=c.precatorio.data_publicacao,
                        foro=c.precatorio.foro,
                        valor_nominal=c.precatorio.valor_nominal
                    ) if c.precatorio else None
                )                    
            )
            for c in db_credores
        ]

    