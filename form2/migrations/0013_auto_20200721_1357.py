# Generated by Django 3.0.8 on 2020-07-21 10:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('form2', '0012_auto_20200721_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form2',
            name='AtanmaTarihi',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2020, 7, 21, 10, 57, 3, 651471, tzinfo=utc), verbose_name='Atanma Tarihi'),
        ),
    ]