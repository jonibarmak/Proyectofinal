from tkinter import CASCADE
from django.db import models

class Products(models.Model):                                                   #modelo para cada zapatilla
    name= models.CharField(max_length=40)                                       #nombre de la zapa
    price= models.FloatField()                                                  #precio de la zapa
    description= models.CharField(max_length=200, null=True, blank=True)        #descripcion de la zapa
    is_active=models.BooleanField(default=True)                     
    creation_date=models.DateField(auto_now_add=True,null=True,blank=True)  
    stock=models.IntegerField()                                                 #cantidad de zapas 
    image=models.ImageField(upload_to="products/",null=True,blank=True)         #imagen de la zapa        
    brand=models.CharField(max_length=40,null=True, blank=True)                 #marca

    def __str__(self): 
        return self.name 
    
    class Meta: 
        verbose_name= "Product" 
        verbose_name_plural= "Products"


class Category(models.Model):
    name= models.CharField(max_length=50)




