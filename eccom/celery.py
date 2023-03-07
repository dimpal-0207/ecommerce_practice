from __future__ import unicode_literals,absolute_import
import os

from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery.settings')

app = Celery('django_celery')
app.conf.enable_utc = False

app.conf.update(timezone='Asia/kolkata')
# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.


app.conf.beat_schedule = {

    'send-mail-every-day-at-8': {
        'task': 'celery_app.tasks.send_mail_func',
        'schedule': crontab(hour=14, minute=41, day_of_month=1, month_of_year=6),
        # 'args': (2,)
    }

}

# CELERY_BEAT_SCHEDULE = {
#     'run-every-day-midnight': {
#         'task': 'your_task_name',
#         'schedule': crontab(hour=0, minute=0, timezone='Asia/Kolkata'),
#     },
# }

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

