class BuscarCredores:
    def __init__(self, credor_repository):
        self.credor_repository = credor_repository

    def execute(self):
        return self.credor_repository.listar_todos()