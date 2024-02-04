import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'phone_finder.settings')

app = Celery('phone_finder')
app.config_from_object('django.conf:settings', namespace="CELERY")
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'every': {
        'task': 'phone_finder.tasks.tables_updater',
        'schedule': crontab(),
    },

}