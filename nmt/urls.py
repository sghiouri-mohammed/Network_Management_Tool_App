from . import views
from django.urls import path, include


urlpatterns = [

    path("", views.login),
    path("Register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("index/", views.index, name="index"),
    path("logout/", views.logout, name="logout"),

]
