from django.urls import path

from . import views

app_name = "contract"

urlpatterns = [
    path('', views.index_managers, name="index_managers"),
    path('update/<int:pk>/', views.ManagerUpdateView.as_view(), name="update_manager"),
    path('delete/<int:pk>/', views.ManagerDeleteView.as_view(), name="delete_manager"),

]
