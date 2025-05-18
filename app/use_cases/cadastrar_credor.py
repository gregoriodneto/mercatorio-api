class CadastrarCredor:
    def __init__(self, credor_repository):
        self.credor_repository = credor_repository

    def execute(self, data):
        return self.credor_repository.adicionar(data)