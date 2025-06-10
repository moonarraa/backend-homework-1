from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    "scrape-salons-everyday": {
        "task": "src.tasks.scrape_salons_task",
        "schedule": crontab(hour=0, minute=0),  # Every day at midnight
    },
}