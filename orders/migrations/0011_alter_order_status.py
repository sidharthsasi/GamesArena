# Generated by Django 4.0.4 on 2022-07-02 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Corfirmed', 'Corfirmed'), ('Accepted', 'Accepted'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled'), ('Returned', 'Returned')], default='Confirmed', max_length=20),
        ),
    ]
