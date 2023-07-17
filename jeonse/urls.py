# jeonse/urls.py

from django.urls import path
from allauth.account import views as allauth_views
from jeonse.views import ListingListView, ListingDetailView, ListingCreateView

urlpatterns = [
    path('accounts/login/', allauth_views.LoginView.as_view(), name='account_login'),
    path('accounts/logout/', allauth_views.LogoutView.as_view(), name='account_logout'),
    path('accounts/signup/', allauth_views.SignupView.as_view(), name='account_signup'),
    path('', ListingListView.as_view(), name="listing_list"),
    path('<int:pk>/', ListingDetailView.as_view(), name="listing_detail"),
    path('create/', ListingCreateView.as_view(), name="listing_create"),
]
