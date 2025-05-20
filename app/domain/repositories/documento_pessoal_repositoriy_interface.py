from abc import ABC, abstractmethod
from app.domain.models.documento_pessoal import DocumentoPessoal

class DocumentoPessoalRepositoryInterface(ABC):
    @abstractmethod
    def adicionar(self, credor: DocumentoPessoal) -> DocumentoPessoal:
        pass

    @abstractmethod
    def documento_adicionado_ao_credor(self, credor_id) -> DocumentoPessoal:
        pass
