import datetime as dt

from django.conf import settings
from django.db import models

from administremos.models import Bus
from contratos.models import Contract


# Create your models here.


class Service(models.Model):
    route_name = models.CharField(max_length=300, verbose_name="name service or route")
    start_date = models.DateTimeField(verbose_name="start date")
    end_date = models.DateTimeField(verbose_name="end date")
    # bus = models.CharField(verbose_name="bus") relevate = models.CharField(verbose_name="Este va a ser el campo de
    # relevo") created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
    # related_name="services_author", verbose_name="created by", null=True)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name="services_contract")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="updated at")

    def __str__(self):
        return self.route_name


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
    day = models.CharField(max_length=2, verbose_name="day")
    service = models.ForeignKey("Service", on_delete=models.CASCADE, related_name="schedules_service")
    bus = models.ForeignKey(Bus, on_delete=models.DO_NOTHING, related_name="schedule", verbose_name="bus", null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING,
                                   related_name="schedules_author", verbose_name="created by", null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="updated at")

    def __str__(self):
        return self.type_schedule


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
