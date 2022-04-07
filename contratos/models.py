import datetime as dt

from django.conf import settings
from django.db import models

from users.models import Manager


class UserContractor(models.Model):
    CONTRACTOR_BY = 'CONTRATANTE'
    CONTRACTOR_FOR = 'CONTRATISTA'
    TYPE_CONTRACTOR = [
        (CONTRACTOR_BY, 'Contratante'),
        (CONTRACTOR_FOR, 'Contratista'),
    ]
    name_entity = models.CharField(max_length=300, verbose_name="name")
    phone = models.CharField(max_length=100, verbose_name="phone number")
    extension = models.CharField(max_length=10, verbose_name="extension")
    nit = models.CharField(max_length=255, verbose_name="company nit")
    type_contractor = models.CharField(max_length=20, choices=TYPE_CONTRACTOR, default=CONTRACTOR_BY)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                                   related_name="user_contractor", verbose_name="created by", null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="updated at")

    def __str__(self):
        return self.name_entity


class FixedContract(models.Model):
    type_contract = models.CharField(max_length=20, default="FIJO")
    contractor_by = models.ForeignKey(UserContractor, on_delete=models.DO_NOTHING, verbose_name="contractor by",
                                      related_name="contract_by_fixed")
    contractor_for = models.ForeignKey(UserContractor, on_delete=models.DO_NOTHING, verbose_name="contractor for",
                                       related_name="contract_for")
    start_date = models.DateTimeField(verbose_name="start date")
    end_date = models.DateTimeField(verbose_name="end date")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="fixedcontract",
                                   verbose_name="created by", null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="updated at")

    def __str__(self):
        return f"{self.contractor_by}"

    # def get_absolute_url(self):
    #     return reverse('', kwargs={'pk': self.pk})


class OccasionalContract(models.Model):
    contractor_by = models.ForeignKey(UserContractor, on_delete=models.DO_NOTHING, verbose_name="contractor by",
                                      related_name="contract_by_occasional")
    nit = models.CharField(max_length=30, verbose_name="nit or cc")
    address = models.CharField(max_length=300, verbose_name="address")
    city = models.CharField(max_length=200, verbose_name="city")
    contact_person = models.CharField(max_length=300, verbose_name="contact")
    contact_phone = models.CharField(max_length=300, verbose_name="contact phone")
    arrival = models.CharField(max_length=300, verbose_name="arrival")
    hour = models.TimeField(default=dt.time(00, 00), verbose_name="end hour")
    date_service = models.DateField(verbose_name="date service")
    capacity = models.IntegerField(verbose_name="capacity")
    go = models.CharField(max_length=300, verbose_name="go")
    come_bak = models.CharField(max_length=300, verbose_name="come_back")
    nro_spreadsheet = models.CharField(max_length=300, verbose_name="spreadsheet number")
    reservation = models.CharField(max_length=300, verbose_name="reservation")
    observations = models.CharField(max_length=300, verbose_name="observations")
    manager = models.ForeignKey(Manager, on_delete=models.DO_NOTHING, related_name="ocasional_contract",
                                verbose_name="manager")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="contract",
                                   verbose_name="created by", null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="updated at")


class Spreadsheet(models.Model):
    number_spreadsheet = models.CharField(max_length=30, verbose_name="number")
    contracts = models.ManyToManyField(FixedContract, related_name="spreadsheets")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="updated at")

    def __str__(self):
        return self.number_spreadsheet
