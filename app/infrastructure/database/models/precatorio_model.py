from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.infrastructure.database.base import Base

class PrecatorioModel(Base):
    __tablename__ = 'precatorios'

    id = Column(Integer, primary_key=True)
    credor_id = Column(Integer, ForeignKey('credores.id'), nullable=False)
    numero_precatorio = Column(String, nullable=False)
    valor_nominal = Column(Float, nullable=False)
    foro = Column(String, nullable=False)
    data_publicacao = Column(Date, nullable=False)

    credor = relationship('CredorModel', back_populates='precatorio')