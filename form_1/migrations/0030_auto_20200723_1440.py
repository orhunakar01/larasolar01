# Generated by Django 3.0.8 on 2020-07-23 11:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('form_1', '0029_auto_20200723_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form1',
            name='baslangic',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 23, 11, 40, 50, 648322, tzinfo=utc)),
        ),
    ]
