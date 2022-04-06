from django.contrib import admin

# Register your models here.


from .models import UserContractor, Contract, Spreadsheet

admin.site.register(UserContractor)
admin.site.register(Contract)
admin.site.register(Spreadsheet)
