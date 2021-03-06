# Generated by Django 4.0.4 on 2022-07-03 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_image', models.ImageField(blank=True, upload_to='photos/banner')),
                ('is_selected', models.BooleanField(default=False)),
            ],
        ),
    ]
