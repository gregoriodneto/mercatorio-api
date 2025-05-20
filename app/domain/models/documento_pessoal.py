class DocumentoPessoal:
    def __init__(self, id, credor_id, tipo, arquivo_url, enviado_em):
        self.id = id
        self.credor_id = credor_id
        self.tipo = tipo
        self.arquivo_url = arquivo_url
        self.enviado_em = enviado_em