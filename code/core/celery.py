import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
app = Celery('core')
app.conf.beat_schedule = {
    'update_data': {
        'task': 'test_task.tasks.update_data',
        'schedule': 30.0,
    },
}
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
