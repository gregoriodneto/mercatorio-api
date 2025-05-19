from sqlalchemy.orm import joinedload
from app.domain.models.precatorio import Precatorio
from app.domain.repositories.precatorio_repositoriy_interface import PrecatorioRepositoryInterface
from app.infrastructure.database.models.credor_model import CredorModel
from app.infrastructure.database.models.precatorio_model import PrecatorioModel
from app.infrastructure.database.db_config import SessionLocal

class PrecatorioRepository(PrecatorioRepositoryInterface):
    def __init__(self):
        self.session = SessionLocal()

    def adicionar(self, precatorio: Precatorio) -> Precatorio:
        db_precatorio = PrecatorioModel(
            credor_id=precatorio.credor_id,
            numero_precatorio=precatorio.numero_precatorio,
            valor_nominal=precatorio.valor_nominal,
            foro=precatorio.foro,
            data_publicacao=precatorio.data_publicacao,
        )
        self.session.add(db_precatorio)
        self.session.commit()
        self.session.refresh(db_precatorio)
        precatorio.id = db_precatorio.id
        return precatorio

    