# Generated by Django 4.0.4 on 2022-06-22 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_alter_orderproduct_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Corfirmed', 'Corfirmed'), ('Accepted', 'Accepted'), ('Completed', 'Completed'), ('Canelled', 'Cancelled')], default='Confirmed', max_length=20),
        ),
    ]
