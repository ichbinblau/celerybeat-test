from __future__ import absolute_import
from celery_proj.celery_app import app
from celery.utils.log import get_task_logger

@app.task(name='celery_proj.tasks.add')
def add(x, y):
    logger = get_task_logger(__name__)
    logger.info('Adding {0} + {1}'.format(x, y))
    print 'Adding {0} + {1}'.format(x, y)
    return x + y




