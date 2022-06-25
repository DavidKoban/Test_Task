Для начала запустите докер-контейнеры
```
docker-compose up -d
docker-compose exec app python manage.py migrate
docker-compose exec app python manage.py shell
```
Далее ввести:
```
from django_celery_beat.models import CrontabSchedule, PeriodicTask
from test_task.tasks import update_data
schedule, created = IntervalSchedule.objects.get_or_create(
    every=10,
    period=IntervalSchedule.SECONDS,
)
PeriodicTask.objects.create(
    interval=schedule,
    name='update_data',
    task='test_task.tasks.update_data',
)
```
После чего для выхода нажмите Crtl+Z(или Crtl+D) и перезагрузите докер-контейнеры
```
docker-compose restart
```

Далее перейдите по ссылке

http://localhost:8000/



P.S.

Обновление данных происходит каждые 10 секунд, для просмотра результата обновления нужно перезагрузить страницу
