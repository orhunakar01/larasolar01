# Generated by Django 3.0.8 on 2020-08-20 08:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('anasayfa', '0003_remove_anasayfa_olusturan'),
    ]

    operations = [
        migrations.AddField(
            model_name='anasayfa',
            name='Olusturan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
