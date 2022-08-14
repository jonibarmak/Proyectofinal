from django import forms

class Formulario_nosotros(forms.Form):
     name=forms.CharField(max_length=40)
     description=forms.CharField(max_length=1000)
     image=forms.ImageField(required=False)