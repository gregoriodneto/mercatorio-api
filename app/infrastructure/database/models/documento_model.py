from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.infrastructure.database.base import Base

class DocumentoModel(Base):
    __tablename__ = 'documentos'

    id = Column(Integer, primary_key=True)
    credor_id = Column(Integer, ForeignKey('credores.id'), nullable=False)
    tipo = Column(String, nullable=False)
    arquivo_url = Column(String, nullable=False)
    enviado_em = Column(Date, nullable=False)

    credor = relationship('CredorModel', back_populates='documentos')