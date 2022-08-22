from tkinter import CASCADE
from django.db import models

class User_profile(models.Model):
    user=models.OneToOneField("auth.User",on_delete=models.CASCADE,related_name="profile")
    name=models.CharField(max_length=30,blank=True)
    lastname=models.CharField(max_length=50,blank=True)
    image=models.ImageField(upload_to="profile_image/",blank=True)

    def __str__(self):
        return f'Perfil de {self.user.username}'



