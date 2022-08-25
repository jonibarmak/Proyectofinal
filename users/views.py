from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from users.forms import User_registration_form,Usereditform
from django.contrib.auth.decorators import login_required
from .models import User_profile

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                
                context = {'message':f'Bienvenido {username} a Orange-Shoes!!'}
                return render(request, 'index.html', context = context)

        form = AuthenticationForm()
        return render(request, 'login.html', {'error': 'Formulario inválido', 'form': form})

    elif request.method == 'GET':
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = User_registration_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            context = {'errors':form.errors}
            form = User_registration_form()
            context['form'] = form
            return render(request, 'register.html', context)
       

    elif request.method == 'GET':
        form=User_registration_form()
        return render(request,"register.html",{'form': form})

    

@login_required
def show_profile(request):
    user=request.user
    form=Usereditform(initial={
            "email":user.email})
    return render(request,"show_profile.html",{"form":form})

@login_required
def edit_profile(request):
    user=request.user
    if request.method == "POST":
        form=Usereditform(request.POST,request.FILES)
        if form.is_valid():            
            user.email=form.cleaned_data["email"]
            user.password1=form.cleaned_data["password1"]
            user.password2=form.cleaned_data["password2"]
            user.first_name=form.cleaned_data["first_name"]
            user.last_name=form.cleaned_data["last_name"]
            user.save()
                                       
            return render(request,"index.html")
       

    else: 
        form=Usereditform(initial={
            "email":user.email,
            "first_name":user.first_name,
            "last_name":user.last_name
            })
        return render(request,"edit_profile.html",{"form":form})








