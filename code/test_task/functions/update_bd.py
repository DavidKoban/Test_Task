from test_task.models import Order
from datetime import datetime

# Функция кторая проходится по всей базе и обновляет значения
def update_db(table_values, db_values):
    # Получаем индекс объекта в базе
    for line in range(len(db_values)):
        # Проверяем соответствуют ли значение в таблице и в базе данных
        if list(db_values[line]) != table_values[line]:
            update_order = Order.objects.get(id=db_values[line][0])
            if db_values[line][1] != table_values[line][1]:# Проверяем на соответствие номер заказа
                update_order.order_number = table_values[line][1]
            if db_values[line][2] != table_values[line][2]:# Проверяем на соответствие цену заказа
                update_order.cost_usd = table_values[line][2]
            if db_values[line][3] != table_values[line][3]:# Проверяем на соответствие дату поставки заказа
                update_order.delivery_time = datetime.strptime(table_values[line][3], '%d.%m.%Y')
            update_order.save()
