# Generated by Django 3.2 on 2022-04-07 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20220406_2235'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ('created_at',)},
        ),
    ]