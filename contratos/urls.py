from django.urls import path

from . import views

app_name = "contract"

urlpatterns = [
    path('fixed/', views.index_contracts_fixed, name="index_contract_fixed"),
    path('occasional/', views.index_contracts_occasional, name="index_contract_occasional"),
    path('occasional/delete/<int:pk>/', views.ContractOccasionalDeleteView.as_view(), name="delete_contract_occasional"),
    path('fixed/<int:pk>/', views.detail_contract_fixed, name="detail_contract_fixed"),
    path('fixed/update/<int:pk>/', views.ContractFixedUpdateView.as_view(), name="update_contract_fixed"),
    path('fixed/delete/<int:pk>/', views.ContractDeleteView.as_view(), name="delete_contract"),
    path('spreadsheet/<int:pk>/', views.spreadsheet, name="spreadsheet"),
]
