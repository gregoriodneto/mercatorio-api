from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger
from app.jobs.revalida_certidoes_job import revalidar_certidoes_job
from dotenv import load_dotenv
import os

load_dotenv()

SCHEDULE_RUN_TRIGGER_INTERVAL_HOURS=os.getenv("SCHEDULE_RUN_TRIGGER_INTERVAL_HOURS")

def start_schedule():
    scheduler = AsyncIOScheduler()

    scheduler.add_job(
        revalidar_certidoes_job,
        trigger=IntervalTrigger(hours=int(SCHEDULE_RUN_TRIGGER_INTERVAL_HOURS)),
        id='revalidar_certidoes_job',
        replace_existing=True
    )

    scheduler.start()