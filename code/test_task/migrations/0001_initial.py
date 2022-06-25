# Generated by Django 3.1.7 on 2022-06-23 11:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('order_number', models.IntegerField(default='0', unique=True)),
                ('cost_usd', models.DecimalField(decimal_places=2, default='0', max_digits=10)),
                ('delivery_time', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]