from django.db import models



class Account(models.Model):

    id = models.AutoField(primary_key=True)
    lastname = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    username = models.EmailField()
    password = models.CharField(max_length=40)