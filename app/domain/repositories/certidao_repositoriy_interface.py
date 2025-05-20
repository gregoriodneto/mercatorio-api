from abc import ABC, abstractmethod
from app.domain.models.certidao import Certidao

class CertidaoRepositoryInterface(ABC):
    @abstractmethod
    def adicionar(self, credor: Certidao) -> Certidao:
        pass
