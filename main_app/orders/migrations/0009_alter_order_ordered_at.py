# Generated by Django 4.0.3 on 2022-04-24 19:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_order_payment_mode_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ordered_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]