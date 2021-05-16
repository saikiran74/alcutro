from django.db import models
from django.contrib.auth.models import User
class fav(models.Model):
    head=models.CharField(max_length=100)
    subheading=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
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

