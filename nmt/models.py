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


class CampusBuildings(models.Model):
    id_campus = models.IntegerField()
    nom = models.CharField(max_length=255)

class DataCenterBuildings(models.Model):
    id_data = models.IntegerField()
    nom = models.CharField(max_length=255)


class ConferenceCenterBuildings(models.Model):
    id_conf = models.IntegerField()
    nom = models.CharField(max_length=255)


class Floor(models.Model):
    id = models.AutoField(primary_key=True)
    floor_name = models.CharField(max_length=255)
    floor_level = models.FloatField()


class Equipement(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    ip = models.CharField(max_length=20)
    model = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    network_center = models.ForeignKey(NetworkCenter, on_delete=models.CASCADE)
    building = models.IntegerField()
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)




