from django.contrib import admin

# Register your models here.

from .models import Service, Schedule, Day

admin.site.register(Service)
admin.site.register(Schedule)
admin.site.register(Day)
