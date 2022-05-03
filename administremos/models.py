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
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="bus_driver",
                                   verbose_name="created by", null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="fecha de actualización")

    class Meta:
        db_table = 'bus'

    def __str__(self):
        return f"{self.code} - {self.name}"

    def check_driver(self):
        return {'id': self.driver.id, 'name': self.driver.name, } if self.driver else {'id': '',
                                                                                       'name': 'No Asignado', }

    def model_to_json(self):
        item = {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'plate': self.plate,
            'brand': self.brand,
            'model': self.model,
            'driver': self.check_driver(),

        }
        return item


class ReliefBus(models.Model):
    bus = models.ForeignKey('Bus', on_delete=models.CASCADE, verbose_name="bus", related_name="relief_bus")
    relief = models.ForeignKey('Bus', on_delete=models.CASCADE, verbose_name="bus", related_name="bus_relief")
    start_date = models.DateTimeField(verbose_name="start date", null=True, blank=True)
    end_date = models.DateTimeField(verbose_name="end date", null=True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="bus_relief",
                                   verbose_name="created by", null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="fecha de actualización")

    class Meta:
        db_table = "relief_bus"

    def __str__(self):
        return self.bus

    def model_to_json(self):
        item = {
            'id': self.id,
            'bus': {'id': self.bus.id, 'name': self.bus.name},
            'relief': {'id': self.relief.id, 'name': self.relief.name},
            'start_date': self.start_date.strftime('%Y-%m-%d'),
            'end_date': self.end_date.strftime('%Y-%m-%d'),
            'created_by': f'{self.created_by.first_name} {self.created_by.last_name}',
        }
        return item


class Driver(models.Model):
    """ Modelo del empleado """
    name = models.CharField(max_length=200, null=True)
    code = models.CharField(max_length=100, null=True)
    id_driver = models.CharField(max_length=50, null=True)
    nro_identification = models.CharField(max_length=50, null=True)
    # This field is for performance and features systems only
    has_relief = models.BooleanField(default=False, verbose_name="has relief?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="fecha de actualización")

    class Meta:
        db_table = 'driver'

    def __str__(self):
        return self.name

    def model_to_json(self):
        item = {
            'id': self.id,
            'driver': {'id': self.id_driver,
                       'name': self.name,
                       },
            'code': self.code,
            'nro_identification': self.nro_identification,
        }
        return item


#
class ReliefDriver(models.Model):
    driver = models.ForeignKey('Driver', on_delete=models.CASCADE, verbose_name="driver", related_name="relief_driver")
    relief = models.ForeignKey('Driver', on_delete=models.CASCADE, verbose_name="driver", related_name="driver_relief")
    start_date = models.DateTimeField(verbose_name="start date", null=True, blank=True)
    end_date = models.DateTimeField(verbose_name="end date", null=True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="driver_relief",
                                   verbose_name="created by", null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="fecha de actualización")

    class Meta:
        db_table = "relief_driver"

    def __str__(self):
        return self.driver.name

    def model_to_json(self):
        item = {
            'id': self.id,
            'driver': {'id': self.driver.id, 'name': self.driver.name},
            'relief': {'id': self.relief.id, 'name': self.relief.name},
            'start_date': self.start_date.strftime('%Y-%m-%d'),
            'end_date': self.end_date.strftime('%Y-%m-%d'),
            'created_by': f'{self.created_by.first_name} {self.created_by.last_name}',
        }
        return item


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

    class Meta:
        db_table = "novelty"

    def __str__(self):
        return self.description

    def model_to_json(self):
        item = {
            'id': self.id,
            'bus': {'id': self.bus.id,
                    'name': f'({self.bus.code})-{self.bus.name}',
                    },
            'start_hour': self.start_hour,
            'end_hour': self.end_hour,
            'start_date': self.start_date.strftime('%Y-%m-%d'),
            'end_date': self.end_date.strftime('%Y-%m-%d'),
            'description': self.description,
            'created_by': f'{self.created_by.first_name} {self.created_by.last_name}',
        }
        return item


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
