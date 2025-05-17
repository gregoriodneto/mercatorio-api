from abc import ABC, abstractmethod
from domain.models.precatorio import Precatorio

class PrecatorioRepositoryInterface(ABC):
    @abstractmethod
    def adicionar(self, credor: Precatorio) -> Precatorio:
        pass

    @abstractmethod
    def obter_por_credor_id(self, credor_id: int) -> list[Precatorio]:
        pass

    @abstractmethod
    def listar_todos(self) -> list[Precatorio]:
        pass
