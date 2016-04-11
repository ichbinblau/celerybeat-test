BROKER_URL='amqp://guest:guest@10.239.76.66:5672'
CELERY_RESULT_BACKEND = 'amqp://'
CELERY_TASK_SERIALIZER='json'
CELERY_ACCEPT_CONTENT=['json']
CELERY_IMPORTS = ("celery_proj.tasks", )
