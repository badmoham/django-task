import os
from celery import Celery
from celery.schedules import solar

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend_interview.settings")
app = Celery("backend_interview")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    # Executes at sunset in Tehran
    'send_report_sms_to_managers': {
        'task': 'tasks.send_restock_sms',
        'schedule': solar('sunset', 35.7219, 51.3347),
    },
}

