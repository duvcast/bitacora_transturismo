# Generated by Django 3.2 on 2022-04-05 16:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0004_auto_20220405_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='schedules_author', to=settings.AUTH_USER_MODEL, verbose_name='created by'),
        ),
    ]
