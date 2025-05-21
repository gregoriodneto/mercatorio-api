import os
from datetime import datetime, timezone
from fastapi import HTTPException
from app.domain.models.documento_pessoal import DocumentoPessoal
from app.interfaces.schemas.documento_schema import DocumentoInput
from app.interfaces.custom.file_verification import validar_arquivo, upload_arquivo

UPLOAD_DIR="uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

class UploadDocumentosPessoais:
    def __init__(self, documentos_repository, credor_repository):
        self.documentos_repository = documentos_repository
        self.credor_repository = credor_repository

    async def execute(self, credor_id: int, documento_input:DocumentoInput, file):
        if file is None:
            raise HTTPException(
                status_code=404,
                detail="Necessário enviar documento pessoal."
            )  

        validar_arquivo(file)  
        
        credor = self.credor_repository.obter_por_id(credor_id)
        if credor is None:
            raise HTTPException(
                status_code=404,
                detail="Credor não existe."
            )

        file_path = await upload_arquivo(
            credor_id=credor_id,
            tipo_arquivo="documento",
            file=file
        )

        documento = DocumentoPessoal(
            id=None,
            credor_id=credor_id,
            tipo=documento_input.tipo,
            arquivo_url=file_path,
            enviado_em=datetime.now(timezone.utc)
        )
        return self.documentos_repository.adicionar(documento)