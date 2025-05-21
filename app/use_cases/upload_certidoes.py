import os
from datetime import datetime, timezone
from fastapi import HTTPException
from app.domain.models.certidao import Certidao
from app.interfaces.schemas.certidao_schema import CertidaoInput
from app.interfaces.custom.file_verification import validar_arquivo, upload_arquivo
from app.infrastructure.services.certidao_api_mock import gerar_certidao_base64, consultar_certidoes_externas

class UploadCertidoes:
    def __init__(self, certidao_repository, credor_repository):
        self.certidao_repository = certidao_repository
        self.credor_repository = credor_repository

    async def execute(self, credor_id: int, certidao_input:CertidaoInput, file):  
        credor = self.credor_repository.obter_por_id(credor_id)
        if credor is None:
            raise HTTPException(
                status_code=404,
                detail="Credor não existe."
            )
        
        try:
            certidoes_cadastradas = []
            if certidao_input.origem == "manual":
                if file is None:
                    raise HTTPException(
                        status_code=404,
                        detail="Necessário enviar a certidao pessoal."
                    ) 
                validar_arquivo(file)

                file_path = await upload_arquivo(
                    credor_id=credor_id,
                    tipo_arquivo="certidao",
                    file=file
                )

                base64 = gerar_certidao_base64(file_path)

                certidao = Certidao(
                    id=None,
                    credor_id=credor_id,
                    tipo=certidao_input.tipo,
                    conteudo_base64=base64,
                    origem=certidao_input.origem,
                    status=certidao_input.status,
                    recebida_em=datetime.now(timezone.utc)
                )
                certidao_cad = self.certidao_repository.adicionar(certidao)
                certidoes_cadastradas.append(certidao_cad)
            elif certidao_input.origem == "api":               
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
                        origem=certidao_input.origem,
                        status=c["status"],
                        recebida_em=datetime.now(timezone.utc)
                    )
                    certidao_cad = self.certidao_repository.adicionar(certidao)
                    certidoes_cadastradas.append(certidao_cad)
            else:
                raise HTTPException(
                    status_code=500,
                    detail="Origem de referência não existe."
                )
            return certidoes_cadastradas
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=str(e)
            ) 