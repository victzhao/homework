from django.db import models

# Create your models here.


class userinfo(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    password= models.CharField(max_length=30)
    phone=models.IntegerField()


class hostinfo(models.Model):
    pass


