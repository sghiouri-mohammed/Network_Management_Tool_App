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
    path('campus/chateau/', views.chateau_details, name='chateau_details'),
    path('campus/marshall_building/', views.marshall_building_details, name='marshall_building_details'),
    path('campus/boulogne/', views.boulogne_details, name='boulogne_details'),
    path('campus/franqueville/', views.chateau_details, name='franqueville_details'),
    path('campus/monaco/', views.monaco_details, name='monaco_details'),
    path('floor/', views.chateau_details, name='floor'),
]