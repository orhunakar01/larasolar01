# Generated by Django 3.0.8 on 2020-07-23 11:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('form4', '0005_auto_20200723_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form4',
            name='tarih',
            field=models.DateField(default=datetime.datetime(2020, 7, 23, 11, 35, 5, 489635, tzinfo=utc), verbose_name="Firma'nın Onaylama Tarihi :"),
        ),
    ]
