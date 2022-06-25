import decimal
from datetime import datetime
from django.views.generic import TemplateView
from pycbrf.toolbox import ExchangeRates
from test_task.models import Order


class Order_View(TemplateView):
    # html файл которой будет отображаться при вызове данного View
    template_name = 'order.html'

    def get_context_data(self, **kwargs):
        # Смомощью сторонней библиотеки получаем данные про сегодняшнюю цену доллара
        exchange_value = ExchangeRates(datetime.today())['USD'].value
        return {
            'orders': [
                {
                    'id': order.id,
                    'order_number': order.order_number,
                    'cost_usd': order.cost_usd,
                    # Добавленное поле стоимость в рублях
                    'cost_rub': (order.cost_usd*exchange_value).quantize(decimal.Decimal("1.00"), decimal.ROUND_05UP),
                    'delivery_time': order.delivery_time,
                }
                # Получаем объекты из базы для вывода на страницу
                for order in Order.objects.all().order_by('id')
            ],
        }