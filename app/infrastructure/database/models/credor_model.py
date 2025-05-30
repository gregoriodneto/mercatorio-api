from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.infrastructure.database.base import Base

class CredorModel(Base):
    __tablename__ = 'credores'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    cpf_cnpj = Column(String, nullable=False)
    email = Column(String, nullable=False)
    telefone = Column(String, nullable=False)

    precatorio = relationship('PrecatorioModel', back_populates='credor', uselist=False)
    documentos = relationship('DocumentoModel', back_populates='credor')
    certidoes = relationship('CertidaoModel', back_populates='credor')