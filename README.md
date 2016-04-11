# celerybeat-test
A sample code to test the celery beat with parameters

run the code by:
celery -A celerybeat_test.tasks worker -l info -B -Q test
