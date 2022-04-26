from django.urls import path

from . import views

app_name = "administremos"

urlpatterns = [
    path('buses/', views.bus, name="buses"),
    path('relief-buses/', views.buses_relief, name="relief_buses"),
    path('drivers/', views.driver, name="drivers"),
    path('remove-driver/', views.remove_bus_driver, name="remove_driver"),
    path('relief-drivers/', views.drivers_relief, name="relief_drivers"),
    path('novelties/', views.novelties, name="novelties"),
    path('create-novelties/', views.create_novelty, name="create_novelty"),
]
