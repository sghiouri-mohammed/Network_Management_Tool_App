from . import views
from django.urls import path, include


urlpatterns = [

    path("", views.login),
    path("Register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("index/", views.index, name="index"),
    path("logout/", views.logout, name="logout"),
    path('campus/', views.campus_details, name='campus_details'),
    path('data-centre/', views.data_centre_details, name='data_centre_details'),
    path('conference-centre/', views.conference_centre_details, name='conference_centre_details'),
    path('campus/chateau/', views.chateau_details, name='campus/chateau_details'),
    path('campus/marshall_building/', views.chateau_details, name='campus/marshall_building_details'),
    path('campus/boulogne/', views.chateau_details, name='campus/boulogne_details'),
    path('campus/franqueville/', views.chateau_details, name='campus/franqueville_details'),
    path('campus/monaco/', views.chateau_details, name='campus/monaco_details'),
]