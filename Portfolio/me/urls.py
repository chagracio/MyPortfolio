from django.urls import path
from . import views

urlpatterns = [
    path('cha_login', views.login_user, name = 'cha_login'),
    path('logout', views.logout_user, name = 'logout'),
]