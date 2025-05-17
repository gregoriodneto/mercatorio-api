from abc import ABC, abstractmethod
from domain.models.certidao import Certidao

class CertidaoRepositoryInterface(ABC):
    @abstractmethod
    def adicionar(self, credor: Certidao) -> Certidao:
        pass

    @abstractmethod
    def obter_por_credor_id(self, credor_id: int) -> list[Certidao]:
        pass

    @abstractmethod
    def listar_todos(self) -> list[Certidao]:
        pass
