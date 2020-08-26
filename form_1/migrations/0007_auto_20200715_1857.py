# Generated by Django 3.0.8 on 2020-07-15 15:57

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('form_1', '0006_auto_20200715_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='form1',
            name='Olusturan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='form1',
            name='baslangic',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 15, 15, 57, 11, 452638, tzinfo=utc)),
        ),
    ]