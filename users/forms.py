from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import User_profile 

class User_registration_form(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        help_texts = {k:'' for k in fields} 

class Usereditform(UserCreationForm):
    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

        help_texts = {k:'' for k in fields} 

class Profile_Form(forms.Form):
    user=forms.CharField(max_length=40)
    name=forms.CharField(max_length=30)
    lastname=forms.CharField(max_length=50)
    image=forms.ImageField(required=False)

