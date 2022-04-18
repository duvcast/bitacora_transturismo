from django.urls import path

from . import views

app_name = "contract"

urlpatterns = [
    path('fixed/', views.index_contracts_fixed, name="index_contract_fixed"),
    path('fixed-list', views.contract_fixed_list, name='contracts_fixed_list'),
    path('fixed-create/', views.create_contract_fixed, name='create_contract_fixed'),
    path('occasional/', views.index_contracts_occasional, name="index_contract_occasional"),
    path('occasional/delete/<int:pk>/', views.ContractOccasionalDeleteView.as_view(),
         name="delete_contract_occasional"),
    path('fixed/<int:pk>/', views.detail_contract_fixed, name="detail_contract_fixed"),
    path('fixed/update/<int:pk>/', views.ContractFixedUpdateView.as_view(), name="update_contract_fixed"),
    path('fixed/delete/<int:pk>/', views.ContractDeleteView.as_view(), name="delete_contract"),
    path('spreadsheet/<int:pk>/', views.spreadsheet, name="spreadsheet"),
    path('users-contacts/', views.users_contract, name="users_contract"),
    path('users-contacts/update/<int:pk>/', views.UserContractUpdateView.as_view(), name="update_users_contract"),
    path('users-contacts/delete/<int:pk>/', views.UserContractorDeleteView.as_view(), name="delete_users_contract"),
]
