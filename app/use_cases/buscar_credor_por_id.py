class BuscarCredorPorId:
    def __init__(self, credor_repository):
        self.credor_repository = credor_repository

    def execute(self, credor_id):
        return self.credor_repository.obter_por_id(credor_id)