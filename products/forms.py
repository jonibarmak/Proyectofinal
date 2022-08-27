from django import forms 


class Formulario_productos(forms.Form):
    name=forms.CharField(max_length=40)
    price=forms.FloatField()
    description=forms.CharField(max_length=200)
    stock=forms.IntegerField()
    brand=forms.CharField(max_length=40)
    image=forms.ImageField(required=False)
   

