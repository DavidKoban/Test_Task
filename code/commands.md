```
docker-compose up -d
docker-compose exec app python manage.py migrate
docker-compose exec app python manage.py shell
>>> from django_celery_beat.models import CrontabSchedule, PeriodicTask
>>> from test_task.tasks import update_data
>>>schedule, created = IntervalSchedule.objects.get_or_create(
    every=10,
    period=IntervalSchedule.SECONDS,
)
>>>PeriodicTask.objects.create(
    interval=schedule,
    name='update_data',
    task='test_task.tasks.update_data',
)
docker-compose down
docker-compose up -d
```
