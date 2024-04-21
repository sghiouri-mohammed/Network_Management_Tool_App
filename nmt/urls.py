from . import views
from django.urls import path, include


urlpatterns = [
    path("", views.login),
    path("login/", views.login),
    path("index/", views.index),

]
