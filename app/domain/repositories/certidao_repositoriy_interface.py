from abc import ABC, abstractmethod
from app.domain.models.certidao import Certidao

class CertidaoRepositoryInterface(ABC):
    @abstractmethod
    def adicionar(self, certidao: Certidao) -> Certidao:
        pass

    @abstractmethod
    def listar_todos(self) -> list[Certidao]:
        pass

    @abstractmethod
    def update_status(self, id: int, status: str) -> Certidao:
        pass
