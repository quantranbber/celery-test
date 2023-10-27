import os
from celery import Celery
import time
import logging
from django.db import connection

logger = logging.getLogger(__name__)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_test.settings')

app = Celery(__name__)
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(name='register')
def execute(store_id, user_id):
    try:
        logger.info("Start logging: %s" % time.ctime())
        cursor = connection.cursor()
        cursor.execute("INSERT INTO store_logdata(store_id, user_id, content) VALUES( %s , %s , %s )",
                       [store_id, user_id, 'testt'])
        logger.info("Success logging: %s" % time.ctime())
    except Exception as e:
        logger.error('Error logging: %s' % e)
