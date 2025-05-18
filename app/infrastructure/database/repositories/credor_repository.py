from app.domain.models.credor import Credor
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
        db_credor = self.session.query(CredorModel).filter_by(id=credor_id).first()
        if db_credor is None:
            return None
        return Credor(
            id=db_credor.id,
            nome=db_credor.nome,
            cpf_cnpj=db_credor.cpf_cnpj,
            email=db_credor.email,
            telefone=db_credor.telefone
        )

    def obter_por_cpf_cnpj(self, cpf_cnpj: str) -> Credor:
        db_credor = self.session.query(CredorModel).filter_by(cpf_cnpj=cpf_cnpj).first()
        if db_credor is None:
            return None
        return Credor(
            id=db_credor.id,
            nome=db_credor.nome,
            cpf_cnpj=db_credor.cpf_cnpj,
            email=db_credor.email,
            telefone=db_credor.telefone
        )

    def listar_todos(self) -> list[Credor]:
        db_credores = self.session.query(CredorModel).all()
        return [
            Credor(
                id=c.id,
                nome=c.nome,
                cpf_cnpj=c.cpf_cnpj,
                email=c.email,
                telefone=c.telefone
            )
            for c in db_credores
        ]

    