# Generated by Django 3.0.7 on 2020-07-07 07:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ilgili_birim', models.CharField(choices=[('Sağlık', 'Sağlık'), ('OSGB', 'OSGB'), ('Diğer', 'Diğer')], max_length=25, verbose_name='İlgili Birim')),
                ('isin_kategorisi', models.CharField(choices=[('ihale', 'ihale'), ('teklif', 'Teklif'), ('Malz.Tedariği', 'Malz.Tedariği'), ('Diğer', 'Diğer')], max_length=25, verbose_name='Yapılan İşin Kategorisi')),
                ('konusu', models.TextField(verbose_name='Konu ile ilgili Açıklama')),
                ('dosya', models.FileField(upload_to='files/')),
                ('sorumlu_kisi', models.CharField(choices=[('cengiz bey', 'Cengiz Bey'), ('tekin bey', 'Tekin Bey'), ('ilhan bey', 'İlhan Bey'), ('mustafa bey', 'Mustafa Bey'), ('diğer', 'Diğer')], max_length=25, verbose_name='İşten Sorumlu Kişi')),
                ('baslangic', models.DateTimeField(default=datetime.datetime(2020, 7, 7, 7, 57, 12, 388429, tzinfo=utc))),
                ('bitis', models.DateTimeField()),
            ],
        ),
    ]
