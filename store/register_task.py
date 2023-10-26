import os

import time
import logging

import psycopg2
from celery import Celery, shared_task
from celery.signals import task_received
from django.apps import apps

logger = logging.getLogger(__name__)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_test.settings')

app = Celery(__name__)
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(name='register')
def run_job(store_id, user_id):
    logger.info("Start logging: %s" % time.ctime())
    print("Start logging: %s" % time.ctime())
    model = apps.get_model(app_label='logData', model_name='LogData')
    new_log = model(store_id=store_id, user_id=user_id, content='success create log')
    new_log.save()


@shared_task
def perform_database_query(store_id, user_id):
    model = apps.get_model(app_label='logData', model_name='LogData')
    new_log = model(store_id=store_id, user_id=user_id, content='success create log')
    new_log.save()
