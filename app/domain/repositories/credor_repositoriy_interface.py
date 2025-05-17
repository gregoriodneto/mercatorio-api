from abc import ABC, abstractmethod
from domain.models.credor import Credor

class CredorRepositoryInterface(ABC):
    @abstractmethod
    def adicionar(self, credor: Credor) -> Credor:
        pass

    @abstractmethod
    def obter_por_id(self, credor_id: int) -> Credor:
        pass

    @abstractmethod
    def obter_por_cpf_cnpj(self, cpf_cnpj: str) -> Credor:
        pass

    @abstractmethod
    def listar_todos(self) -> list[Credor]:
        pass
