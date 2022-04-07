# Generated by Django 3.2 on 2022-04-06 21:26

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FixedContract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_contract', models.CharField(default='FIJO', max_length=20)),
                ('start_date', models.DateTimeField(verbose_name='start date')),
                ('end_date', models.DateTimeField(verbose_name='end date')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
            ],
        ),
        migrations.CreateModel(
            name='UserContractor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_entity', models.CharField(max_length=300, verbose_name='name')),
                ('phone', models.CharField(max_length=100, verbose_name='phone number')),
                ('extension', models.CharField(max_length=10, verbose_name='extension')),
                ('nit', models.CharField(max_length=255, verbose_name='company nit')),
                ('type_contractor', models.CharField(choices=[('CONTRATANTE', 'Contratante'), ('CONTRATISTA', 'Contratista')], default='CONTRATANTE', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_contractor', to=settings.AUTH_USER_MODEL, verbose_name='created by')),
            ],
        ),
        migrations.CreateModel(
            name='Spreadsheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_spreadsheet', models.CharField(max_length=30, verbose_name='number')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('contracts', models.ManyToManyField(related_name='spreadsheets', to='contratos.FixedContract')),
            ],
        ),
        migrations.CreateModel(
            name='OccasionalContract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nit', models.CharField(max_length=30, verbose_name='nit or cc')),
                ('address', models.CharField(max_length=300, verbose_name='address')),
                ('city', models.CharField(max_length=200, verbose_name='city')),
                ('contact_person', models.CharField(max_length=300, verbose_name='contact')),
                ('contact_phone', models.CharField(max_length=300, verbose_name='contact phone')),
                ('arrival', models.CharField(max_length=300, verbose_name='arrival')),
                ('hour', models.TimeField(default=datetime.time(0, 0), verbose_name='end hour')),
                ('date_service', models.DateField(verbose_name='date service')),
                ('capacity', models.IntegerField(verbose_name='capacity')),
                ('go', models.CharField(max_length=300, verbose_name='go')),
                ('come_bak', models.CharField(max_length=300, verbose_name='come_back')),
                ('nro_spreadsheet', models.CharField(max_length=300, verbose_name='spreadsheet number')),
                ('reservation', models.CharField(max_length=300, verbose_name='reservation')),
                ('observations', models.CharField(max_length=300, verbose_name='observations')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('contractor_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='contract_by_occasional', to='contratos.usercontractor', verbose_name='contractor by')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contract', to=settings.AUTH_USER_MODEL, verbose_name='created by')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='ocasional_contract', to='users.manager', verbose_name='manager')),
            ],
        ),
        migrations.AddField(
            model_name='fixedcontract',
            name='contractor_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='contract_by_fixed', to='contratos.usercontractor', verbose_name='contractor by'),
        ),
        migrations.AddField(
            model_name='fixedcontract',
            name='contractor_for',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='contract_for', to='contratos.usercontractor', verbose_name='contractor for'),
        ),
        migrations.AddField(
            model_name='fixedcontract',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fixedcontract', to=settings.AUTH_USER_MODEL, verbose_name='created by'),
        ),
    ]
