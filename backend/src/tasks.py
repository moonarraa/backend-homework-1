from .celery_app import celery
from .services import fetch_salons

@celery.task
def fetch_salons_task():
    return fetch_salons()