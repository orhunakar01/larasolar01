# Generated by Django 3.0.8 on 2020-08-20 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form2', '0035_auto_20200805_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form2',
            name='Sorumlusu',
            field=models.CharField(choices=[('adana', 'adana'), ('cengizyilmaz', 'cengizyilmaz'), ('orhunakar', 'orhunakar'), ('yetkisiz', 'yetkisiz')], max_length=25, verbose_name='Sorumlu Kişiyi Ata'),
        ),
    ]