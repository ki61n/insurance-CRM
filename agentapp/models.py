from django.db import models
from adminapp.models import users,Campain

# Create your models here.

class client(models.Model):
    campain=models.ForeignKey(Campain,on_delete=models.CASCADE,null=True,blank=True)
    agent=models.ForeignKey(users,on_delete=models.CASCADE,null=True,blank=True,related_name='clients_as_agent')
    user=models.ForeignKey(users,on_delete=models.CASCADE,null=True,blank=True,related_name='client_profiles')
    anualIncome=models.IntegerField(null=True,blank=True)
    marrage=models.CharField(max_length=10,null=True,blank=True)
    children=models.IntegerField(null=True,blank=True)
    education=models.CharField(max_length=10,null=True,blank=True)
    occupation=models.CharField(max_length=10,null=True,blank=True)
    otherpolicy=models.CharField(max_length=10,null=True,blank=True)
    policynumber=models.CharField(max_length=10,null=True,blank=True)
    changePolicy=models.CharField(max_length=10,null=True,blank=True)
    clientRating=models.IntegerField(null=True,blank=True)