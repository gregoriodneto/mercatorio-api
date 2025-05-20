import os
from datetime import datetime, timezone
from fastapi import HTTPException
from app.domain.models.documento_pessoal import DocumentoPessoal
from app.interfaces.schemas.documento_schema import DocumentoInput

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
        
        credor = self.credor_repository.obter_por_id(credor_id)
        if credor is None:
            raise HTTPException(
                status_code=404,
                detail="Credor não existe."
            )
        
        documento_cadastrado_credor = self.documentos_repository.documento_adicionado_ao_credor(credor_id)
        if documento_cadastrado_credor:
            raise HTTPException(
                status_code=404,
                detail="Documento já cadastrado no credor informado."
            )

        contents = await file.read()
        file_path = f"{UPLOAD_DIR}/uploads_{file.filename}"
        with open(file_path, "wb") as f:
            f.write(contents)

        documento = DocumentoPessoal(
            id=None,
            credor_id=credor_id,
            tipo=documento_input.tipo,
            arquivo_url=file_path,
            enviado_em=datetime.now(timezone.utc)
        )
        return self.documentos_repository.adicionar(documento)