# Generated by Django 3.0.8 on 2020-07-21 10:57

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('form_1', '0016_auto_20200721_1357'),
        ('form3', '0004_auto_20200721_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form3',
            name='Form33',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='form_1.Form1'),
        ),
        migrations.AlterField(
            model_name='form3',
            name='tarih',
            field=models.DateField(default=datetime.datetime(2020, 7, 21, 10, 57, 3, 651471, tzinfo=utc), verbose_name='Bugünkü Tarih'),
        ),
    ]
