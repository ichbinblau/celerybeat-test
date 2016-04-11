from __future__ import absolute_import

from celery import Celery
from celery_proj import celery_schedule

app = Celery('tasks')
app.config_from_object('celery_proj.celeryconfig')

# Optional configuration, see the application user guide.
app.conf.update(
     CELERY_TASK_RESULT_EXPIRES=3600,
     CELERYBEAT_SCHEDULE=celery_schedule.CELERYBEAT_SCHEDULE,
)
