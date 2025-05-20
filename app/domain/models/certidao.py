class Certidao:
    def __init__(self, id, credor_id, tipo, origem, arquivo_url, status, recebida_em):
        self.id = id
        self.credor_id = credor_id
        self.tipo = tipo
        self.origem = origem
        self.arquivo_url = arquivo_url
        self.status = status
        self.recebida_em = recebida_em