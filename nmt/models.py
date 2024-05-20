from django.db import models

class Account(models.Model):

    id = models.AutoField(primary_key=True)
    lastname = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    mail = models.EmailField(default="admin@gmail.com")
    password = models.CharField(max_length=40)






class NetworkCenter(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)


class Building(models.Model):
    id = models.AutoField(primary_key=True)
    id_network_center = models.IntegerField()
    building_name = models.CharField(max_length=255)
    info = models.CharField(max_length=500,null=True)





class Floor(models.Model):
    id = models.AutoField(primary_key=True)
    id_network_center = models.IntegerField()
    id_building = models.IntegerField()
    nom = models.CharField(max_length=30)
    floor = models.IntegerField()
    info = models.CharField(max_length=500, null=True)


class Local(models.Model):
    id = models.AutoField(primary_key=True)
    id_network_center = models.IntegerField()
    id_building = models.IntegerField()
    id_floor_salle = models.IntegerField()
    nom = models.CharField(max_length=30)
    info = models.CharField(max_length=500, null=True)




class Equipement(models.Model):
    id = models.AutoField(primary_key=True)
    id_network_center = models.IntegerField()
    id_building = models.IntegerField()
    id_floor_salle = models.IntegerField()
    id_local = models.IntegerField()
    nom = models.CharField(max_length=30)
    ip = models.CharField(max_length=20)
    model = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    # serial_number = models.CharField(max_length=255)
    # ios_version = models.CharField(max_length=255)
    info = models.CharField(max_length=500, null=True)


class Commands(models.Model):
    id = models.AutoField(primary_key=True)
    command_name = models.CharField(max_length=500)