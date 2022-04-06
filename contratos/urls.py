from django.urls import path

from . import views

app_name = "contract"

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:pk>/', views.detail_contract, name="detail_contract"),
    path('update/<int:pk>/', views.ContractUpdateView.as_view(), name="update_contract"),
    path('delete/<int:pk>/', views.ContractDeleteView.as_view(), name="delete_contract"),
    path('spreadsheet/<int:pk>/', views.spreadsheet, name="spreadsheet"),
]
