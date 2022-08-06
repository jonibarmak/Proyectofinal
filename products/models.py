from django.conf import settings
from django.db import models

class Products(models.Model):
    name= models.CharField(max_length=40)
    price= models.FloatField()
    description= models.CharField(max_length=40)
    stock=models.IntegerField() 

