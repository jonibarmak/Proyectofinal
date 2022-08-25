from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import User_profile 
from django.forms import ModelForm

class User_registration_form(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    first_name=forms.CharField(label='Nombre')
    last_name=forms.CharField(label='Apellido')
    
    

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2','first_name','last_name')

        help_texts = {k:'' for k in fields} 

class Usereditform(UserCreationForm):
    email = forms.EmailField(label="E-mail")
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    first_name=forms.CharField(label='Nombre')
    last_name=forms.CharField(label='Apellido')
    
    
    
    

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2','first_name','last_name')

        help_texts = {k:'' for k in fields} 


class User_profile_Form(ModelForm):
    class Meta:
        model = User_profile
        fields = ['name','lastname','email','image']