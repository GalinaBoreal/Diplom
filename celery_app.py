import os
import time

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'netology_pd_diplom.settings')

app = Celery('backend')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_url = settings.CELERY_BROKER_URL
app.autodiscover_tasks() #автоматический поиск по всем папкам своих тасков

# для проверки работы селери
@app.task
def debug_task():
    time.sleep(20)
    print('Hello from debug_task!')