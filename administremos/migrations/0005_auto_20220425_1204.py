# Generated by Django 3.2 on 2022-04-25 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administremos', '0004_reliefdriver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reliefdriver',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='end date'),
        ),
        migrations.AlterField(
            model_name='reliefdriver',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='start date'),
        ),
    ]