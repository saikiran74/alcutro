from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model

class All(models.Model):
    head=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    subheading=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    favourite=models.ManyToManyField(User,related_name="Favourite")
    category=models.CharField(max_length=100)
    category1=models.CharField(max_length=100,default=None)
    category2=models.CharField(max_length=100,default=None)
    google=models.BooleanField(default=False)
    microsoft=models.BooleanField(default=False)
    socialmedia=models.BooleanField(default=False)
    adobe=models.BooleanField(default=False)
    apple=models.BooleanField(default=False)
    Other=models.BooleanField(default=False)
    date=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.url


class Contactus(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    querry=models.CharField(max_length=500)

    def __str__(self):
        return self.name
