# Generated by Django 4.0.4 on 2022-06-07 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_zip'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order',
            new_name='user',
        ),
    ]
