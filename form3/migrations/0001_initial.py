# Generated by Django 3.0.8 on 2020-07-21 06:48

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Form3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isin_kategorisi', models.CharField(choices=[('ihale', 'ihale'), ('teklif', 'Teklif'), ('Malz.Tedariği', 'Malz.Tedariği'), ('Diğer', 'Diğer')], max_length=25, verbose_name='İşin Kategorisi')),
                ('Aciklama', models.TextField(blank=True, verbose_name='Açıklama')),
                ('dosya', models.FileField(blank=True, db_index=True, upload_to='')),
                ('tarih', models.DateField(default=datetime.datetime(2020, 7, 21, 6, 48, 35, 967094, tzinfo=utc), verbose_name='Bugünkü Tarih')),
                ('Olusturan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]