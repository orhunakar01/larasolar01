# Generated by Django 3.0.8 on 2020-07-22 14:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('form3', '0012_auto_20200722_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form3',
            name='tarih',
            field=models.DateField(default=datetime.datetime(2020, 7, 22, 14, 23, 59, 557052, tzinfo=utc), verbose_name='Bugünkü Tarih'),
        ),
    ]
