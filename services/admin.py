from django.contrib import admin

# Register your models here.

from .models import Service, Schedule

admin.site.register(Service)
admin.site.register(Schedule)