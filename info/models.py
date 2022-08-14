from django.db import models

class about_us(models.Model):
    image=models.ImageField(upload_to="aboutus/",null=True,blank=True)
    name= models.CharField(max_length=40)
    description= models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name 
    
    class Meta: 
        verbose_name= "Nosotros" 
        verbose_name_plural= "Nosotros" 
