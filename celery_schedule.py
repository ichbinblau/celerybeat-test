from datetime import timedelta

CELERYBEAT_SCHEDULE = {
    'add': {
        'task': 'celery_proj.tasks.add',
        'schedule': timedelta(seconds=3),
        'args': (16, 16),
        'options': {'queue' : 'test'},
    },
}
