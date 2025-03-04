from django.urls import path
from .views import home, live_code_review

urlpatterns = [
    path("", home, name="home"),  # Home page where users submit code
    path("live_review/", live_code_review, name="live_code_review"),  # API endpoint
    # path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('register/', views.register, name='register'),
    # path('profile/', views.profile, name='profile'),
]


# def home(request):
#     return render(request, "review/code_submit.html") 