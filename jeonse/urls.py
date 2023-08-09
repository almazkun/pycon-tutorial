from allauth.account import views as allauth_views
from django.urls import path

urlpatterns = [
    path("accounts/login/", allauth_views.LoginView.as_view(), name="account_login"),
    path("accounts/logout/", allauth_views.LogoutView.as_view(), name="account_logout"),
    path("accounts/signup/", allauth_views.SignupView.as_view(), name="account_signup"),
]
