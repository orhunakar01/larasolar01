# Generated by Django 3.0.8 on 2020-07-23 07:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('form_1', '0026_auto_20200723_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form1',
            name='baslangic',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 23, 7, 8, 22, 403307, tzinfo=utc)),
        ),
    ]
