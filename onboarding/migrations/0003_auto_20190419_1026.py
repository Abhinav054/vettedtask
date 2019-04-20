# Generated by Django 2.0.3 on 2019-04-19 10:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onboarding', '0002_auto_20190419_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companies', to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
