from django.urls import path

from . import views

app_name = "contract"

urlpatterns = [
    path('fixed-contracts/', views.FixedContractView.as_view(), name="fixed_contracts"),
    path('occasional-contracts/', views.OccasionalContractView.as_view(), name="occasional_contracts"),
    path('users-contracts/', views.UserContractsView.as_view(), name="users_contracts"),
    path('spreadsheet/', views.spreadsheet, name="spreadsheet"),
]
