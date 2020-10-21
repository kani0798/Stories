from __future__ import absolute_import, unicode_literals

import os
import django
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

from stories_test.settings import broken_url

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stories_test.settings')
app = Celery('stories_test', broker=broken_url)

app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
  print('Request: {0!r}'.format(self.request))
  print('hello world')


app.conf.beat_schedule = {
    'update-every-1-hour': {
        'task': 'summarize',
        'schedule': 3600.0,
    }
}
