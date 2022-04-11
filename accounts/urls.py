from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path(r"login/$", auth_views.LoginView.as_view(template_name="accounts/login.html"),name='login'),
    path(r"logout/$", auth_views.LogoutView.as_view(), name="logout"),
    path(r"signup/$", views.SignUp.as_view(), name="signup"),
]
