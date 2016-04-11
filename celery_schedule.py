from datetime import timedelta

CELERYBEAT_SCHEDULE = {
    'add': {
        'task': 'celerybeat_test.tasks.add',
        'schedule': timedelta(seconds=3),
        'args': (16, 16),
        'options': {'queue' : 'test'},
    },
}
