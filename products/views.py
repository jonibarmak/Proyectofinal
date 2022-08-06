from django import forms
from django.shortcuts import redirect, render
from products.models import Products 
from products.forms import Formulario_productos 


def create_product(request):
     if request.method=="POST":
        form=Formulario_productos(request.POST)
        if form.is_valid():
            Products.objects.create(
                name=form.cleaned_data["name"],
                description=form.cleaned_data["description"],
                price=form.cleaned_data["price"],
                stock=form.cleaned_data["stock"]                
            )
            return redirect(list_products)

     elif request.method=="GET":
        form=Formulario_productos()
        context={"form":form}
        return render(request,"new_product.html",context=context)

def list_products(request):
    products= Products.objects.all()
    context={
        "products":products
    }
    return render(request,"products_list.html",context=context)

def primer_formulario(request):
    if request.method =="POST":
        Products.objects.create(name=request.POST["name"])
    return render(request,"primer_formulario.html",context={})


