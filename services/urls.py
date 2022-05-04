from django.urls import path

from . import views

app_name = "services"

urlpatterns = [
    path('services/', views.ServiceView.as_view(), name="services"),
    # path('schedule/update/<int:pk>/', views.UpdateScheduleView.as_view(), name="update_schedule"),

]
