import datetime as dt

from django.conf import settings
from django.db import models

from administremos.models import Bus
from contratos.models import FixedContract

# Create your models here.


"""
si envio 1, 2, 3
calculo primero cuantas semanas hay en la fecha inicial del servicio  y fecha final del servicio (2)
tomo el numero day y creo un Schedule con el dia que me pasaron y lo creo el numero de 
veces que me indica el numero de semanas
hora inicial = 3
hora final = 4

semana = 2
dia = 4
para day en 2:
crea un schedule con el numero de day
hora inicial 
hora final 
fecha inicial del servicio 
fecha final del servicio
el dias = [4]
fecha_inicial_servicio = 2022/03/30
d = fecha_inicial_servicio
for dia in dias:
    for i in numero_semanas:
        next_day = next_weekday(d, dia)
        schedule = Schedule.objects.create(start_hour=hora_inicial, end_hour=hora_final, day=dia, date=next_day)
        d = schedule.date

"""


class Service(models.Model):
    route_name = models.CharField(max_length=300, verbose_name="name service or route")
    start_date = models.DateTimeField(verbose_name="start date")
    end_date = models.DateTimeField(verbose_name="end date")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                                   related_name="services_author", verbose_name="created by", null=True)
    contract = models.ForeignKey(FixedContract, on_delete=models.CASCADE, related_name="services_contract")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="updated at")

    class Meta:
        db_table = 'service'
        ordering = ('-created_at',)

    def __str__(self):
        return self.route_name

    def model_to_json(self):
        item = {
            'id': self.id,
            'route_name': self.route_name,
            'start_date': self.start_date.strftime('%Y-%m-%d'),
            'end_date': self.end_date.strftime('%Y-%m-%d'),
            'contract': self.contract.model_to_json(),
            'created_by': f'{self.created_by.first_name} {self.created_by.last_name}',
        }
        return item


class Schedule(models.Model):
    DEPARTURE = 'SACA'
    ARRIVAL = 'ENTRA'
    TYPE_SCHEDULE = [
        (DEPARTURE, 'Saca'),
        (ARRIVAL, 'Entra'),
    ]
    type_schedule = models.CharField(max_length=30, choices=TYPE_SCHEDULE, default=DEPARTURE,
                                     verbose_name="schedule type")
    start_hour = models.TimeField(default=dt.time(00, 00), verbose_name="end hour")
    end_hour = models.TimeField(default=dt.time(00, 00), verbose_name="end hour")
    quantity_fleet = models.IntegerField(verbose_name="quantity fleet", default=1)
    service = models.ForeignKey("Service", on_delete=models.CASCADE, related_name="schedules_service")
    bus = models.ForeignKey(Bus, on_delete=models.DO_NOTHING, related_name="schedule", verbose_name="bus", null=True)
    day = models.ManyToManyField('Day', related_name="schedule_day")  # fisrt model name plus field relationship
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING,
                                   related_name="schedules_author", verbose_name="created by", null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="updated at")

    def __str__(self):
        return self.type_schedule

    class Meta:
        db_table = 'schedule'
        ordering = ('-created_at',)


class Day(models.Model):
    name = models.CharField(max_length=20, verbose_name="name day")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                                   related_name="days_author", verbose_name="created by", null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="updated at")

    class Meta:
        db_table = 'day'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name

    def model_to_json(self):
        item = {
            'id': self.id,
            'name': self.name,
            'service': self.service.model_to_json(),
            'created_by': f'{self.created_by.first_name} {self.created_by.last_name}',
        }
        return item
