from __future__ import absolute_import
from celerybeat_test.celery_app import app
from celery.utils.log import get_task_logger

@app.task(name='celerybeat_test.tasks.add')
def add(x, y):
    logger = get_task_logger(__name__)
    logger.info('Adding {0} + {1}'.format(x, y))
    #print 'Adding {0} + {1}'.format(x, y)
    return x + y




