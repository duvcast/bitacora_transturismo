import datetime as dt

from django.conf import settings
from django.db import models


class Bus(models.Model):
    """
    Modelo Bus
    """
    id_active = models.CharField(max_length=50)
    name = models.CharField(max_length=200, null=True)
    code = models.CharField(max_length=100, null=True)
    plate = models.CharField(max_length=100, null=True)
    brand = models.CharField(max_length=100, null=True)
    model = models.CharField(max_length=100, null=True)
    driver = models.ForeignKey('Driver', on_delete=models.SET_NULL, related_name='bus', null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="fecha de actualización")

    class Meta:
        db_table = 'bus'

    def __str__(self):
        return f"{self.code} - {self.name}"


class Driver(models.Model):
    """ Modelo del empleado """
    name = models.CharField(max_length=200, null=True)
    code = models.CharField(max_length=100, null=True)
    id_driver = models.CharField(max_length=50, null=True)
    nro_identification = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="fecha de actualización")

    class Meta:
        db_table = 'driver'

    def __str__(self):
        return self.name


# class ReliefDriver(models.Model):
# driver = models.OneToOneField(Driver, on_delete=models.CASCADE, primary_key=True, unique=True)
# relief = models.OneToOneField(Driver, on_delete=models.CASCADE, primary_key=True, unique=True)


class Relief(models.Model):
    driver = models.OneToOneField('Driver', on_delete=models.CASCADE, verbose_name="driver", related_name="relief")
    created_date = models.DateTimeField(verbose_name="date creation")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="fecha de actualización")

    class Meta:
        db_table = "relief"

    def __str__(self):
        return self.driver


class Novelty(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, related_name="bus")
    start_date = models.DateField(verbose_name="start date")
    start_hour = models.TimeField(default=dt.time(00, 00), verbose_name="start hour")
    end_date = models.DateField(verbose_name="end date")
    end_hour = models.TimeField(default=dt.time(00, 00), verbose_name="end hour")
    description = models.TextField(verbose_name="description")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="novelty",
                                   verbose_name="created by", null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="fecha de actualización")


class DetectionMode(models.Model):
    name = models.CharField(max_length=200, null=True)
    code = models.CharField(max_length=100, null=True)
    id_detection_mode = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="fecha de actualización")

    class Meta:
        db_table = 'detection_mode'


class ControlVariable(models.Model):
    """ Modelo de Variable Control"""
    name = models.CharField(max_length=200, null=True)
    code = models.CharField(max_length=100, null=True)
    id_control_variable = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="fecha de actualización")

    class Meta:
        db_table = 'control_variable'


class Symptom(models.Model):
    """Modelo de Sintomas"""
    nombre = models.CharField(max_length=200, null=True)
    codigo = models.CharField(max_length=100, null=True)
    id_symptom = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="fecha de actualización")

    class Meta:
        db_table = 'symptom'


class OperationPlace(models.Model):
    """Modelo lugar de operacion"""
    name = models.CharField(max_length=200, null=True)
    code = models.CharField(max_length=100, null=True)
    id_operation_place = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="fecha de actualización")

    class Meta:
        db_table = 'operation_place'
