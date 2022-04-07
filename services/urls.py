from django.urls import path

from . import views

app_name = "services"

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:pk>/', views.detail_service, name="detail_service"),
    path('delete/<int:pk>/', views.ServiceDeleteView.as_view(), name="delete_service"),
    path('update/<int:pk>/', views.UpdateServiceView.as_view(), name="update_service"),
    path('schedule/delete/<int:pk>/', views.DeleteScheduleView.as_view(), name="delete_schedule"),
    # path('schedule/update/<int:pk>/', views.UpdateScheduleView.as_view(), name="update_schedule"),

]
