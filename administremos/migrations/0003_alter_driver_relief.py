# Generated by Django 3.2 on 2022-04-25 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administremos', '0002_auto_20220424_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='relief',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='administremos.driver'),
        ),
    ]