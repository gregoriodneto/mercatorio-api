from abc import ABC, abstractmethod
from app.domain.models.precatorio import Precatorio

class PrecatorioRepositoryInterface(ABC):
    @abstractmethod
    def adicionar(self, credor: Precatorio) -> Precatorio:
        pass
