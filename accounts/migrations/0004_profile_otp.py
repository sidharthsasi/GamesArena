# Generated by Django 4.0.4 on 2022-05-31 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='otp',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]