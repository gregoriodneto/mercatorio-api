class Certidao:
    def __init__(self, id, credor_id, tipo, origem, conteudo_base64, status, recebida_em):
        self.id = id
        self.credor_id = credor_id
        self.tipo = tipo
        self.origem = origem
        self.conteudo_base64 = conteudo_base64
        self.status = status
        self.recebida_em = recebida_em