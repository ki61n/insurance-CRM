from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import User

# Create your models here.

class users(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    phone=models.CharField(max_length=15,null=True,blank=True)
    address=models.TextField(null=True,blank=True)
    gender=models.CharField(max_length=10,null=True,blank=True)
    dob=models.DateField(null=True,blank=True)
    profile=models.ImageField(upload_to='profile',null=True,blank=True)
    aadhar=models.CharField(max_length=12,null=True,blank=True)
    pan=models.CharField(max_length=10,null=True,blank=True)



class Campain(models.Model):
    agent=models.ForeignKey(users,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=100,null=True,blank=True)
    place=models.CharField(max_length=100,null=True,blank=True)
    date=models.DateField(null=True,blank=True)
    time=models.TimeField(null=True,blank=True)
    image=models.ImageField(upload_to='campain',null=True,blank=True)
