from fastapi import UploadFile, File, HTTPException

ALLOWED_EXTENSIONS = {"pdf", "jpg", "jpeg", "png"}
MAX_FILE_SIZE_MB = 5

async def validar_arquivo(file: UploadFile = File(...)):
    filename = file.filename
    extension = filename.rsplit(".", 1)[-1].lower()
    if extension is not ALLOWED_EXTENSIONS:
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
