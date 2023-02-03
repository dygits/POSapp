# Generated by Django 4.0.3 on 2022-05-21 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_id'),
        ('orders', '0009_alter_order_ordered_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='ingredient_order',
        ),
        migrations.AddField(
            model_name='order',
            name='product_order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
    ]