from tkinter import CASCADE
from django.db import models


class Products(models.Model):
    name= models.CharField(max_length=40)
    price= models.FloatField()
    description= models.CharField(max_length=200, null=True, blank=True)
    is_active=models.BooleanField(default=True)
    creation_date=models.DateField(auto_now_add=True,null=True,blank=True)
    stock=models.IntegerField()
    image=models.ImageField(upload_to="products/",null=True,blank=True)
   
    def __str__(self): 
        return self.name 
    
    class Meta: 
        verbose_name= "Product" 
        verbose_name_plural= "Products"
        
        
class Category(models.Model):
    name= models.CharField(max_length=50)

class Brand(models.Model):
    name=models.CharField(max_length=100)


