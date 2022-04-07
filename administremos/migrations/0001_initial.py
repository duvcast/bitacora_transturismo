# Generated by Django 3.2 on 2022-04-06 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_activo', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=200, null=True)),
                ('codigo', models.CharField(max_length=100, null=True)),
                ('placa', models.CharField(max_length=100, null=True)),
                ('marca', models.CharField(max_length=100, null=True)),
                ('modelo', models.CharField(max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='fecha de actualización')),
            ],
            options={
                'db_table': 'bus',
            },
        ),
        migrations.CreateModel(
            name='BusDriver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='fecha de actualización')),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administremos.bus', verbose_name='bus')),
            ],
            options={
                'db_table': 'bus_driver',
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, null=True)),
                ('codigo', models.CharField(max_length=100, null=True)),
                ('id_empleado', models.CharField(max_length=50, null=True)),
                ('nro_identificacion', models.CharField(max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='fecha de actualización')),
            ],
            options={
                'db_table': 'driver',
            },
        ),
        migrations.CreateModel(
            name='LugaresOperacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, null=True)),
                ('codigo', models.CharField(max_length=100, null=True)),
                ('id_lugar_operacion', models.CharField(max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='fecha de actualización')),
            ],
            options={
                'db_table': 'lugares_operacion',
            },
        ),
        migrations.CreateModel(
            name='ModosDeteccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, null=True)),
                ('codigo', models.CharField(max_length=100, null=True)),
                ('id_modo_deteccion', models.CharField(max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='fecha de actualización')),
            ],
            options={
                'db_table': 'modo_deteccion',
            },
        ),
        migrations.CreateModel(
            name='Sintomas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, null=True)),
                ('codigo', models.CharField(max_length=100, null=True)),
                ('id_sintoma', models.CharField(max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='fecha de actualización')),
            ],
            options={
                'db_table': 'sintomas',
            },
        ),
        migrations.CreateModel(
            name='VariablesControl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, null=True)),
                ('codigo', models.CharField(max_length=100, null=True)),
                ('id_variable_control', models.CharField(max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='fecha de actualización')),
            ],
            options={
                'db_table': 'variables_control',
            },
        ),
        migrations.CreateModel(
            name='Relief',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='fecha de actualización')),
                ('driver', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='administremos.busdriver', verbose_name='driver')),
            ],
            options={
                'db_table': 'relief',
            },
        ),
        migrations.AddField(
            model_name='busdriver',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administremos.empleado', verbose_name='empleado'),
        ),
    ]
