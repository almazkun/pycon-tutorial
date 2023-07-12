# jeonse/urls.py

from django.urls import path
from allauth.account import views as allauth_views

urlpatterns = [
    path('accounts/login/', allauth_views.LoginView.as_view(), name='account_login'),
    path('accounts/logout/', allauth_views.LogoutView.as_view(), name='account_logout'),
    path('accounts/signup/', allauth_views.SignupView.as_view(), name='account_signup'),
    path('accounts/password/reset/', allauth_views.PasswordResetView.as_view(), name='account_reset_password'),
    path('accounts/email/change/', allauth_views.EmailView.as_view(), name='account_email'),
]