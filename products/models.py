from tkinter import CASCADE
from django.db import models


""" class Brand(models.Model):
    name=models.CharField(max_length=100)
    class Meta:
        verbose_name= "Brand" 
        verbose_name_plural='Brands'

    def __str__(self):
        return self.name """

class Products(models.Model):
    name= models.CharField(max_length=40)
    price= models.FloatField()
    description= models.CharField(max_length=200, null=True, blank=True)
    is_active=models.BooleanField(default=True)
    creation_date=models.DateField(auto_now_add=True,null=True,blank=True)
    stock=models.IntegerField()
    image=models.ImageField(upload_to="products/",null=True,blank=True)
    #brand=models.ForeignKey(Brand,on_delete=models.CASCADE,blank=True,default="")
   
    def __str__(self): 
        return self.name 
    
    class Meta: 
        verbose_name= "Product" 
        verbose_name_plural= "Products"


class Category(models.Model):
    name= models.CharField(max_length=50)




