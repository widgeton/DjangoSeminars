# Generated by Django 4.2.4 on 2023-08-25 16:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seminar2_app1', '0002_alter_coin_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 25, 19, 2, 56, 435927)),
        ),
    ]
