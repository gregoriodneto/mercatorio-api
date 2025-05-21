from fastapi import HTTPException
from datetime import datetime, timezone
from app.infrastructure.services.certidao_api_mock import consultar_certidoes_externas
from app.domain.models.certidao import Certidao

class BuscarCertidoes:
    def __init__(self, credor_repository):
        self.credor_repository = credor_repository

    def execute(self, credor_id):
        credor = self.credor_repository.obter_por_id(credor_id)
        if credor is None:
            raise HTTPException(
                status_code=404,
                detail="Credor não existe."
            )
        certidoes_cadastradas = []
        certidoes_api = consultar_certidoes_externas(cpf_cnpj=credor.cpf_cnpj)
        if "certidoes" not in certidoes_api:
            raise HTTPException(
                status_code=500,
                detail="Api externa não retornou certidões."
            )
        for c in certidoes_api["certidoes"]:
            certidao = Certidao(
                id=None,
                credor_id=credor_id,
                tipo=c["tipo"],
                conteudo_base64=c["conteudo_base64"],
                origem="api",
                status=c["status"],
                recebida_em=datetime.now(timezone.utc)
            )
            certidoes_cadastradas.append(certidao)
        return certidoes_cadastradas
        
