# Generated by Django 3.0.8 on 2020-07-23 07:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('form3', '0016_auto_20200723_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form3',
            name='tarih',
            field=models.DateField(default=datetime.datetime(2020, 7, 23, 7, 10, 32, 290743, tzinfo=utc), verbose_name='Bugünkü Tarih'),
        ),
    ]
