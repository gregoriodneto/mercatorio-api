import os
from datetime import datetime, timezone
from fastapi import HTTPException
from app.domain.models.certidao import Certidao
from app.interfaces.schemas.certidao_schema import CertidaoInput
from app.infrastructure.services.certidao_api_mock import gerar_certidao_base64, consultar_certidoes

UPLOAD_DIR="uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

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
            if certidao_input.origem == "manual":
                if file is None:
                    raise HTTPException(
                        status_code=404,
                        detail="Necessário enviar a certidao pessoal."
                    )  
                contents = await file.read()
                file_path = f"{UPLOAD_DIR}/uploads_{file.filename}"
                with open(file_path, "wb") as f:
                    f.write(contents)

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
                self.certidao_repository.adicionar(certidao)
            else:
                certidoes_api = consultar_certidoes(cpf_cnpj=credor.cpf_cnpj)
                for c in certidoes_api:
                    certidao = Certidao(
                        id=None,
                        credor_id=credor_id,
                        tipo=c.tipo,
                        conteudo_base64=gerar_certidao_base64(c.conteudo_base64),
                        origem=certidao_input.origem,
                        status=c.status,
                        recebida_em=datetime.now(timezone.utc)
                    )
                    self.certidao_repository.adicionar(certidao)
            
            return None
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=str(e)
            ) 