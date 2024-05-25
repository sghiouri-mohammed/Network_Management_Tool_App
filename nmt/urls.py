from . import views
from django.urls import path, include


urlpatterns = [

    path("", views.login),
    path("Register/", views.register, name="register"),

    path("login/", views.login, name="login"),

    path("index/", views.index, name="index"),

    path("home/", views.home, name="home"),

    path("Network Centers/", views.netwok_centers, name="config"),
    path("Delete_center/<int:id_center>", views.delete_network_center, name="delete_network_center"),

    path("Buildings/<int:id_center>", views.buildings, name="buildings"),
    path("Delete_Buildings/<int:id_building>", views.delete_building, name="delete_building"),

    path("Floors/<int:id_center>/<int:id_building>", views.floor, name="floors"),
    path("Delete_floor/<int:id_floor>", views.delete_floor, name="delete_floor"),

    path("Locals/<int:id_center>/<int:id_building>/<int:id_floor>", views.local, name="locals"),
    path("Delete_local/<int:id_local>", views.delete_local, name="delete_local"),

    path("Switches/<int:id_center>/<int:id_building>/<int:id_floor>/<int:id_local>", views.equipement, name="equipments"),
    path("Delete_Material/<int:id_equipment>", views.delete_local, name="delete_equipment"),

    path("Add_NC/", views.add_network_center, name="add_nc"),
    path("Add_Building/", views.add_building, name="add_building"),
    path("Add_Floor_Room/", views.add_floor_room, name="add_floor_room"),

    path("Details_Switch/", views.details_equipement, name="detail_equi"),
    path("SSH_Connexion/", views.ssh_connexion, name="ssh_connexion"),





    path("devices/", views.devices, name="devices"),
    path("AddFloor/", views.addfloor, name="addfloor"),
    path("logout/", views.logout, name="logout"),
    path('campus/', views.campus_details, name='campus_details'),
    path('data-centre/', views.data_centre_details, name='data_centre_details'),
    path('conference-centre/', views.conference_centre_details, name='conference_centre_details'),
    path('campus/chateau/', views.chateau_details, name='chateau_details'),
    path('campus/marshall_building/', views.marshall_building_details, name='marshall_building_details'),
    path('campus/boulogne/', views.boulogne_details, name='boulogne_details'),
    path('campus/franqueville/', views.franqueville_details, name='franqueville_details'),
    path('campus/octave_feuillet/', views.octave_feuillet_details, name='octave_feuillet_details'),
    path('campus/monaco/', views.monaco_details, name='monaco_details'),
    path('campus/chateau/basement', views.ch_basement_details, name='ch_basement_details'),
    path('campus/chateau/ground_floor', views.ch_ground_floor_details, name='ch_ground_floor_details'),
    path('campus/chateau/third_floor', views.ch_third_floor_details, name='ch_third_floor_details'),
    path('campus/marshall_building/basement', views.mb_basement_details, name='mb_basement_details'),
    path('campus/marshall_building/ground_floor', views.mb_ground_floor_details, name='mb_ground_floor_details'),
    path('campus/marshall_building/first_floor', views.mb_first_floor_details, name='mb_first_floor_details'),
    path('campus/marshall_building/second_floor', views.mb_second_floor_details, name='mb_second_floor_details'),
    path('campus/marshall_building/third_floor', views.mb_third_floor_details, name='mb_third_floor_details'),
    path('campus/marshall_building/fourth_floor', views.mb_fourth_floor_details, name='mb_fourth_floor_details'),
    path('campus/marshall_building/fifth_floor', views.mb_fifth_floor_details, name='mb_fifth_floor_details'),
   path('campus/marshall_building/sixth_floor', views.mb_sixth_floor_details, name='mb_sixth_floor_details'),
    path('floor/', views.floor_details, name='floor'),
]