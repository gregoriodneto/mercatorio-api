from abc import ABC, abstractmethod
from domain.models.documento_pessoal import DocumentoPessoal

class DocumentoPessoalRepositoryInterface(ABC):
    @abstractmethod
    def adicionar(self, credor: DocumentoPessoal) -> DocumentoPessoal:
        pass

    @abstractmethod
    def obter_por_credor_id(self, credor_id: int) -> list[DocumentoPessoal]:
        pass

    @abstractmethod
    def listar_todos(self) -> list[DocumentoPessoal]:
        pass
