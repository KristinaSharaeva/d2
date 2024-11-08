# Generated by Django 5.1.2 on 2024-11-03 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='phone_number',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='registration_date',
            new_name='registered_at',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='order_date',
            new_name='ordered_at',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='total_amount',
            new_name='total_price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='added_date',
            new_name='added_at',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='title',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(to='shop.product'),
        ),
    ]
