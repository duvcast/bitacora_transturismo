import datetime
from django.utils import timezone

from django.db import models
from django.urls import reverse


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
    # created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
    # related_name="user_contractor", verbose_name="created by", null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="updated at")

    def __str__(self):
        return self.name_entity


class Contract(models.Model):
    DEFAULT_CONTRACTOR_FOR_ID = 2
    FIXED = 'FIJO'
    OCCASIONAL = 'OCASIONAL'
    TYPE_CONTRACT = [
        (FIXED, 'Fijo'),
        (OCCASIONAL, 'Ocasional'),
    ]
    number_contract = models.CharField(max_length=30, verbose_name="number contract")
    type_contract = models.CharField(max_length=20, choices=TYPE_CONTRACT, default=FIXED)
    contractor_by = models.ForeignKey(UserContractor, on_delete=models.DO_NOTHING, verbose_name="contractor by",
                                      related_name="contract_by")
    contractor_for = models.ForeignKey(UserContractor, on_delete=models.DO_NOTHING, verbose_name="contractor for",
                                       related_name="contract_for", default=DEFAULT_CONTRACTOR_FOR_ID)
    start_date = models.DateTimeField(verbose_name="start date")
    end_date = models.DateTimeField(verbose_name="end date")
    arrival = models.CharField(max_length=300, verbose_name="arrival")
    departure = models.CharField(max_length=300, verbose_name="departure")
    # created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="contract",
    #                                verbose_name="created by", null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="updated at")

    def __str__(self):
        return self.number_contract

    # def get_absolute_url(self):
    #     return reverse('', kwargs={'pk': self.pk})


class Spreadsheet(models.Model):
    number_spreadsheet = models.CharField(max_length=30, verbose_name="number")
    contracts = models.ManyToManyField(Contract, related_name="spreadsheets")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="updated at")

    def __str__(self):
        return self.number_spreadsheet

# class OccasionalContract(models.Model):
#     contract = models.ForeignKey('Contract', on_delete=models.CASCADE, related_name="occasional_contract",
#                                  verbose_name="contract")


