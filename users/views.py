from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from users.forms import User_registration_form, Formulario_profile
from django.http import HttpResponse
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

def show_profile(request):
    #if request.user.is_authenticated:
        #return HttpResponse(request.user.profile.phone)
    profile= User_profile.objects.get()
    context={"profile":profile}
    return render(request,"show_profile.html",context=context)

@login_required      
def create_profile(request):
        if request.method=="POST":
            form=Formulario_profile(request.POST,request.FILES)
            if form.is_valid():
                User_profile.objects.create(
                user=form.cleaned_data["user"],
                phone=form.cleaned_data["phone"],
                adress=form.cleaned_data["adress"],
                image=form.cleaned_data["image"]                  
            )
                return redirect(show_profile)


        elif request.method=="GET": 
            form=Formulario_profile()
            context={"form":form}
            return render(request,"create_profile.html",context=context) 

@login_required
def update_profile(request):
    if request.method=="POST":
        form=Formulario_profile(request.POST,request.FILES)
        if form.is_valid():
            profile= User_profile.objects.get()
            profile.user=form.cleaned_data["user"]
            profile.phone=form.cleaned_data["phone"]              
            profile.adress=form.cleaned_data["adress"]
            profile.image=form.cleaned_data["image"] 
            
            profile.save()

            return redirect(show_profile) 


    elif request.method=="GET":
        profile=User_profile.objects.get()
        form=Formulario_profile(initial={
            "user":profile.user,
            "phone":profile.phone,
            "adress":profile.adress})
        context={"form":form}
        return render(request,"update_profile.html",context=context)

def descripction_profile(request):
    if request.method == 'GET':
        profile = User_profile.objects.get()
        context = {'profile':profile}
        return render(request, 'detalles_perfil.html', context=context) 
    
