# Generated by Django 4.2.4 on 2023-08-23 12:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flip', models.BooleanField()),
                ('time', models.DateTimeField(default=datetime.datetime(2023, 8, 23, 15, 9, 21, 573184))),
            ],
        ),
    ]
