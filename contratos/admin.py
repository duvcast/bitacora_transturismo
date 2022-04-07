from django.contrib import admin

# Register your models here.


from .models import UserContractor, FixedContract, Spreadsheet

admin.site.register(UserContractor)
admin.site.register(FixedContract)
admin.site.register(Spreadsheet)
