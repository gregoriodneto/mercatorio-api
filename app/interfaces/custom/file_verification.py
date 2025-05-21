from fastapi import UploadFile, File, HTTPException
import os, uuid

ALLOWED_EXTENSIONS = {"pdf", "jpg", "jpeg", "png"}
MAX_FILE_SIZE_MB = 5

UPLOAD_DIR="uploads"
os.makedirs(UPLOAD_DIR + "/documento", exist_ok=True)
os.makedirs(UPLOAD_DIR + "/certidao", exist_ok=True)
ALLOWED_TYPES_DOCS = { "documento", "certidao" }

async def validar_arquivo(file: UploadFile = File(...)):
    filename = file.filename
    extension = filename.rsplit(".", 1)[-1].lower()
    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"Extensão de arquivo não permitida: {extension}. Permitidas: {', '.join(ALLOWED_EXTENSIONS)}"
        )

    contents = await file.read()
    file_size_mb = len(contents) / (1024 * 1024)
    if file_size_mb > MAX_FILE_SIZE_MB:
        raise HTTPException(
            status_code=400,
            detail=f"Tamanho limite do arquivo de {MAX_FILE_SIZE_MB}"
        )
    await file.seek(0)
    return file

async def upload_arquivo(credor_id: int, tipo_arquivo: str, file: UploadFile = File(...)):
    if tipo_arquivo not in ALLOWED_TYPES_DOCS:
        raise HTTPException(
            status_code=400,
            detail=f"Tipo de arquivo não permitido: {tipo_arquivo}. Permitidas: {', '.join(ALLOWED_TYPES_DOCS)}"
        )

    contents = await file.read()
    _,ext = os.path.splitext(file.filename)
    unique_file = f"{tipo_arquivo}_{credor_id}_{uuid.uuid4().hex}{ext}"
    file_path = os.path.join(UPLOAD_DIR + "/" + tipo_arquivo, unique_file)
    with open(file_path, "wb") as f:
        f.write(contents)

    return file_path