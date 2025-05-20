from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.infrastructure.database.base import Base

class CertidaoModel(Base):
    __tablename__ = 'certidoes'

    id = Column(Integer, primary_key=True)
    credor_id = Column(Integer, ForeignKey('credores.id'), nullable=False)
    tipo = Column(String, nullable=False)
    origem = Column(String, nullable=False)
    status = Column(String, nullable=False)
    conteudo_base64 = Column(String, nullable=False)
    recebida_em = Column(Date, nullable=False)

    credor = relationship('CredorModel', back_populates='certidoes')