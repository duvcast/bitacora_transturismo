from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = "main"

urlpatterns = [
    path('login/', views.LoginUserView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
]
