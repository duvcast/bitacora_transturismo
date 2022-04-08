from django.urls import path

from . import views

app_name = "administremos"

urlpatterns = [
    path('buses/', views.bus, name="buses"),
    path('drivers/', views.driver, name="driver"),

]
