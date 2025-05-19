class Credor:
    def __init__(self, id, nome, cpf_cnpj, email, telefone, precatorios = []):
        self.id = id
        self.nome = nome
        self.cpf_cnpj = cpf_cnpj
        self.email = email
        self.telefone = telefone
        self.precatorios = precatorios