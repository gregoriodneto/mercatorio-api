from app.infrastructure.database.repositories.certidao_repository import CertidaoRepository
from datetime import datetime, timezone
from dotenv import load_dotenv
import os, logging

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

DAYS_UPDATE_CERTIDAO_JOB = int(os.getenv('DAYS_UPDATE_CERTIDAO_JOB'))

TYPES_STATUS_VERIFY = {"negativa", "invalida"}

async def revalidar_certidoes_job():
    logger.info("🔄 Iniciando a relavidação de certidões...")
    repo = CertidaoRepository()

    logger.info("📥 Carregando as certidões do banco de dados...")
    certidoes = repo.listar_todos()

    total = len(certidoes)
    logger.info(f"🔎 {total} certidões encontradas.")

    for certidao in certidoes:
        dias_passados = (datetime.now(timezone.utc).date() - certidao.recebida_em).days
        logger.info(f"📝 Analisando Certidão ID: {certidao.id} | Status: {certidao.status} | Dias passados: {dias_passados}")

        if certidao.status in TYPES_STATUS_VERIFY and dias_passados >= DAYS_UPDATE_CERTIDAO_JOB:
            logger.info(f"✅ Certidão ID {certidao.id} elegível para atualização. Alterando status para 'positiva'...")
            repo.update_status(certidao.id, "positiva")
        else:
            logger.info(f"❌ Certidão ID {certidao.id} não atende aos critérios para atualização.")
    logger.info("🏁 Finalizando busca de certidões!")