from django.db import models

# Create your models here.


class Author(models.Model):
    GenderArray = (
        (0, u"男",),
        (1, u"女",),
    )
    name = models.CharField(max_length=30)
    gender = models.IntegerField(choices=GenderArray,)
    age = models.IntegerField()
    email = models.EmailField()
    mobile = models.CharField(max_length=60)
    def __str__(self):
        return self.name



class Publisher(models.Model):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    province = models.CharField(max_length=10)
    city = models.CharField(max_length=24)
    website = models.URLField()
    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=60)
    publisher = models.ForeignKey("Publisher")
    author= models.ManyToManyField("Author")
    publishtime = models.DateField()
    ctime = models.DateTimeField(auto_now_add=True)
    mtime = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name



