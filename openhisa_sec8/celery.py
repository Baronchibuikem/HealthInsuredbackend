from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab


#set the default django settings module for the 'celery' program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.development_settings')

app = Celery('openhisa_sec8')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace = 'CELERY')


# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

app.conf.beat_schedule = {
    # Executes every Monday morning at 8:30 a.m.
    'send-three-months-reminder-email': {
        'task': 'app_enrollment.tasks.send_three_months_reminder',
        'schedule': crontab(hour=8, minute=30, day_of_week=1),
    },
    # executes daily at midnight
    'account-expiry': {
        'task': 'app_enrollment.tasks.expire_user_plans',
        'schedule': crontab(minute=0, hour=0),
    },
    # executes daily at 6:30 a.m
    'policy-payment-due': {
        'task': 'app_enrollment.tasks.policy_payment_due',
        'schedule': crontab(hour=6, minute=30),
    },
}