from __future__ import absolute_import, unicode_literals
from datetime import datetime
from celery import shared_task
from test_task.functions.get_table_values.get_table_values import get_table_values
from test_task.functions.update_bd import update_db
from test_task.models import Order
'''
PeriodicTask.objects.create(
    interval=schedule,
    name='update_data',
    task='test_task.tasks.update_data',
)
'''
# Обновленние данных на странице(для получения данных после этой операции нужно обновить страницу)
@shared_task
def update_data():
    # Получаем значение из таблицы
    table_values = get_table_values()
    # Получаем данные из базы
    db_values = Order.objects.order_by('id').values_list('id', 'order_number', 'cost_usd', 'delivery_time')
    # Вычесляем колличество заказов\длинну полученого масива и кортежа
    len_table_values = len(table_values)
    len_bd_values = len(db_values)
    # Сравниваем колличество заказов
    if len_table_values >= len_bd_values:
        # Данные тех заказов которые уже есть в таблице обновляем
        update_db(table_values, db_values)
        # Создаем новые заказы по полученным выше данным
        if len_table_values > len_bd_values:
            creating_objects_attr = table_values[-(len_table_values - len_bd_values):]
            for line in creating_objects_attr:
                Order.objects.create(
                    id=line[0],
                    order_number=line[1],
                    cost_usd=line[2],
                    delivery_time=datetime.strptime(line[3], '%d.%m.%Y')
                )

    else:
        # Если в таблице заказов меньше чем в базе
        difference_db_and_table_len = len_bd_values - len_table_values
        # Удаляем элементы что бы колиичество елементов в базе и в таблице совпадали
        Order.objects.filter(pk__in=Order.objects.order_by('-id')[:difference_db_and_table_len]).delete()
        # Получаем новый список элементов в базе и обновляем их
        db_values = Order.objects.order_by('id').values_list('id', 'order_number', 'cost_usd', 'delivery_time')
        update_db(table_values, db_values)
