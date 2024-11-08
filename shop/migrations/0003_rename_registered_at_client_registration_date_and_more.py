# Generated by Django 5.1.2 on 2024-11-03 07:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_rename_phone_number_client_phone_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='registered_at',
            new_name='registration_date',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='ordered_at',
            new_name='order_date',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='total_price',
            new_name='total_amount',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='added_at',
            new_name='added_date',
        ),
        migrations.AlterField(
            model_name='order',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.client'),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
