from django.shortcuts import render, redirect
from info.models import about_us
from info.forms import Formulario_nosotros
from django.contrib.auth.decorators import login_required

@login_required
def route_about(request):
    if request.user.is_superuser:
     if request.method=="POST":
        form=Formulario_nosotros(request.POST,request.FILES)
        if form.is_valid():
            about_us.objects.create(
               name=form.cleaned_data["name"],
               description=form.cleaned_data["description"],
               image=form.cleaned_data["image"],)
            return redirect(list_us)

     elif request.method=="GET":
        form=Formulario_nosotros()
        context={"form":form}
        return render(request,"route_about.html",context=context)
    else:
        return redirect(list_us)


def list_us(request):
    people= about_us.objects.all()
    context={
        "people":people
    }
    return render(request,"people_list.html",context=context)