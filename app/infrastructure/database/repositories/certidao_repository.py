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

    