from django.db import models

# Create your models here.


class Author(models.Model):
    GenderArray = (
        (0, u"男",),
        (1, u"女",),
    )
    name = models.CharField(max_length=30)
    gender = models.CharField(choices=GenderArray,max_length=10, default=0)
    age = models.IntegerField()
    email = models.EmailField()
    mobile = models.CharField(max_length=60)



class Publisher(models.Model):
    pass

class Book(models.Model):
    pass

