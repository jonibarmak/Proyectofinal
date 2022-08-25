from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from users.forms import User_registration_form,Usereditform,User_profile_Form
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
    profile = get_object_or_404(User_profile,user=request.user)
    form = User_profile_Form(instance=profile) 
    context = {'form':form}         
    return render(request,"show_profile.html",context)


@login_required
def create_profile(request):
    if request.method=='GET':
        form = User_profile_Form()
        context = {
        'form' : form,
        }
    else:
        form = User_profile_Form(request.POST, request.FILES)
        if form.is_valid():
            User_profile.objects.create(
                    user = request.user,
                    name = form.cleaned_data['name'],
                    lastname = form.cleaned_data['lastname'],
                    email = form.cleaned_data['email'],
                    image = form.cleaned_data['image']
            )
            return render(request,"index.html")
    return render(request,'create_profile.html',context)

@login_required
def edit_profile(request):
    profile = get_object_or_404(User_profile,user=request.user)
    if request.method == 'GET':
        form = User_profile_Form(instance=profile)
        context = {'form':form,'profile':profile}
        return render (request,'edit_profile.html',context)
    else:
        form = User_profile_Form(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            profile.save()
            return render(request,"index.html")

@login_required
def delete_profile(request):
    profile = get_object_or_404(User_profile,user=request.user)
    if request.method == 'GET':
        mensaje = 'Esta por borrar el perfil'
        form = User_profile_Form(instance=profile)
        context = {'form':form,'mensaje':mensaje}
        return render (request,'delete_profile.html',context)
    else:
        profile.delete()
        return render(request,"index.html")





