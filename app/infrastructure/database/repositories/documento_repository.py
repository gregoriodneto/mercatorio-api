from sqlalchemy.orm import joinedload
from app.domain.models.documento_pessoal import DocumentoPessoal
from app.domain.repositories.documento_pessoal_repositoriy_interface import DocumentoPessoalRepositoryInterface
from app.infrastructure.database.models.documento_model import DocumentoModel
from app.infrastructure.database.db_config import SessionLocal

class DocumentoRepository(DocumentoPessoalRepositoryInterface):
    def __init__(self):
        self.session = SessionLocal()

    def adicionar(self, documento: DocumentoPessoal) -> DocumentoPessoal:
        db_documento = DocumentoModel(
            credor_id=documento.credor_id,
            tipo=documento.tipo,
            arquivo_url=documento.arquivo_url,
            enviado_em=documento.enviado_em,
        )
        self.session.add(db_documento)
        self.session.commit()
        self.session.refresh(db_documento)
        documento.id = db_documento.id
        return documento
    
    def documento_adicionado_ao_credor(self, credor_id) -> DocumentoPessoal:
        db_documento = (
            self.session.query(DocumentoModel)
            .filter(DocumentoModel.credor_id == credor_id)
            .order_by(DocumentoModel.enviado_em.desc())
            .first()
        )
        if db_documento:
            return DocumentoPessoal(
                id=db_documento.id,
                credor_id=db_documento.credor_id,
                arquivo_url=db_documento.arquivo_url,
                tipo=db_documento.tipo,
                enviado_em=db_documento.enviado_em
            )
        return None

    