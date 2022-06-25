from django.db import models
from django.utils import timezone


# Модель заказа
class Order(models.Model):
    # № в таблице
    id = models.IntegerField(null=False, primary_key=True, unique=True)
    # Номер заказа
    order_number = models.IntegerField(null=False, default="0", unique=True)
    # Стоимость в долларах
    cost_usd = models.DecimalField(null=False, default="0", max_digits=10, decimal_places=2)
    # Срок поставки
    delivery_time = models.DateField(null=False, default=timezone.now)
