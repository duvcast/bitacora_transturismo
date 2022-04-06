# Generated by Django 3.2 on 2022-04-01 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_contract', models.CharField(max_length=30, verbose_name='number contract')),
                ('type_contract', models.CharField(choices=[('FIJO', 'Fijo'), ('OCASIONAL', 'Ocasional')], default='FIJO', max_length=20)),
                ('start_date', models.DateTimeField(verbose_name='start date')),
                ('end_date', models.DateTimeField(verbose_name='end date')),
                ('arrival', models.CharField(max_length=300, verbose_name='arrival')),
                ('departure', models.CharField(max_length=300, verbose_name='departure')),
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
            ],
        ),
        migrations.CreateModel(
            name='Spreadsheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_spreadsheet', models.CharField(max_length=30, verbose_name='number')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('contracts', models.ManyToManyField(related_name='spreadsheets', to='contratos.Contract')),
            ],
        ),
        migrations.AddField(
            model_name='contract',
            name='contractor_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='contract_by', to='contratos.usercontractor', verbose_name='contractor by'),
        ),
        migrations.AddField(
            model_name='contract',
            name='contractor_for',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.DO_NOTHING, related_name='contract_for', to='contratos.usercontractor', verbose_name='contractor for'),
        ),
    ]
