from django.urls import path

from . import views

app_name = "administremos"

urlpatterns = [
    path('buses/', views.BusView.as_view(), name="buses"),
    path('relief-buses/', views.ReliefBusView.as_view(), name="relief_buses"),
    path('drivers/', views.DriversView.as_view(), name="drivers"),
    path('relief-drivers/', views.ReliefDriversView.as_view(), name="relief_drivers"),
    path('novelties/', views.NoveltyView.as_view(), name="novelties"),
]
