from django.db import models

# Create your models here.


class userinfo(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    password= models.CharField(max_length=30)
    phone=models.IntegerField()


class hostinfo(models.Model):
    hostname = models.CharField(max_length=30)
    ip = models.CharField(max_length=30)
    port = models.IntegerField()
    cpu = models.CharField(max_length=30)
    mem = models.CharField(max_length=30)
    disk = models.CharField(max_length=30)
    status = models.CharField(max_length=10)



