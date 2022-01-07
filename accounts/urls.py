from django import template
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import LoginFormView

urlpatterns = [
    path('login', LoginFormView.as_view(), name='login'),
    path('register', views.register, name='register'),
    path('logout', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
]