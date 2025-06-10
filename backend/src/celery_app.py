from celery import Celery
import os
from .celery_beat_schedule import CELERY_BEAT_SCHEDULE

celery = Celery(
    "zapis",
    broker=os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0"),
    backend=os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379/0"),
)
celery.conf.timezone = "UTC"
celery.conf.beat_schedule = CELERY_BEAT_SCHEDULE