from app.domain.models.certidao import Certidao
from app.domain.repositories.certidao_repositoriy_interface import CertidaoRepositoryInterface
from app.infrastructure.database.models.certidao_model import CertidaoModel
from app.infrastructure.database.db_config import SessionLocal

class CertidaoRepository(CertidaoRepositoryInterface):
    def __init__(self):
        self.session = SessionLocal()

    def adicionar(self, certidao: Certidao) -> Certidao:
        db_certidao = CertidaoModel(
            credor_id=certidao.credor_id,
            tipo=certidao.tipo,
            origem=certidao.origem,
            status=certidao.status,
            conteudo_base64=certidao.conteudo_base64,
            recebida_em=certidao.recebida_em,
        )
        self.session.add(db_certidao)
        self.session.commit()
        self.session.refresh(db_certidao)
        certidao.id = db_certidao.id
        return certidao
    
    def listar_todos(self) -> list[Certidao]:
        db_certidoes = self.session.query(CertidaoModel).all()
        return [
            Certidao(
                id=c.id,
                conteudo_base64=c.conteudo_base64,
                credor_id=c.credor_id,
                origem=c.origem,
                recebida_em=c.recebida_em,
                status=c.status,
                tipo=c.tipo
            ) for c in db_certidoes
        ]
    
    def update_status(self, id: int, status: str) -> Certidao:
        db_certidao = self.session.query(CertidaoModel).filter_by(id=id).first()
        if db_certidao is None:
            return None
        db_certidao.status = status
        self.session.commit()
        self.session.refresh(db_certidao)
        return db_certidao

    