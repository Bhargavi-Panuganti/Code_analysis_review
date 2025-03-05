from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.register, name="register"),  # Default page: Register
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),  # Protected Dashboard
    path("profile/", views.profile, name="profile"),  # Protected Profile
    path("live_review/", views.live_code_review, name="live_code_review"),  # API endpoint
]
