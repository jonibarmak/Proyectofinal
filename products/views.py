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

def search_products(request):
    search=request.GET["search"]
    products=Products.objects.filter(name__icontains=search)
    context={"products":products}
    return render(request,"search_product.html",context=context)

def inicio(request):

    return render(request,"inicio.html")

def borrar_producto(request, id):
    if request.method == 'GET':
        product = Products.objects.get(id=id)
        context = {'product':product}
        return render(request, 'borrar.html', context=context)
    elif request.method == 'POST':
        product = Products.objects.get(id=id)
        product.delete()
        return redirect(list_products)

def descripction_product(request, id):
    if request.method == 'GET':
        product = Products.objects.get(id=id)
        context = {'product':product}
        return render(request, 'detalles.html', context=context)


