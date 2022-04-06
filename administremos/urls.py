from django.urls import path

from . import views

app_name = "administremos"

urlpatterns = [
    path('', views.index, name="index"),
    path('buses/', views.bus, name="buses"),
    path('empleados/', views.empleado, name="empleados"),
    path('bus_drivers/', views.bus_driver, name="bus_drivers"),

]
