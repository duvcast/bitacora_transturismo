from django.urls import path

from . import views

app_name = "contract"

urlpatterns = [
    path('fixed-create/', views.create_fixed_contract, name="create_fixed_contract"),
    path('fixed-list/', views.contracts_fixed_list, name="contracts_fixed_list"),
    path('fixed-delete/', views.contract_fixed_delete, name="contracts_fixed_delete"),
    path('occasional/', views.index_contracts_occasional, name="index_contract_occasional"),
    path('occasional/update/<int:pk>/', views.ContractOccasionalUpdateView.as_view(),
         name="update_contract_occasional"),
    path('occasional/delete/<int:pk>/', views.ContractOccasionalDeleteView.as_view(),
         name="delete_contract_occasional"),
    path('fixed/<int:pk>/', views.detail_contract_fixed, name="detail_contract_fixed"),
    path('fixed/update/<int:pk>/', views.ContractFixedUpdateView.as_view(), name="update_contract_fixed"),
    path('fixed/delete/<int:pk>/', views.ContractDeleteView.as_view(), name="delete_contract"),
    path('users-contacts/', views.users_contract, name="users_contract"),
    path('users-contacts/update/<int:pk>/', views.UserContractUpdateView.as_view(), name="update_users_contract"),
    path('users-contacts/delete/<int:pk>/', views.UserContractorDeleteView.as_view(), name="delete_users_contract"),
    path('spreadsheet/', views.spreadsheet, name="spreadsheet"),
]
