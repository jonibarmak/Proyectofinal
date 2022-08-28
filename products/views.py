from django import forms
from django.shortcuts import redirect, render
from products.models import Products
from products.forms import Formulario_productos
from django.contrib.auth.decorators import login_required
from products.Cart import Cart


@login_required
def create_product(request):                                                        #funcion de creacion de productos
    if request.user.is_superuser:
     if request.method=="POST":
        form=Formulario_productosrequest.FILES(request.POST,)
        if form.is_valid():
            Products.objects.create(
                name=form.cleaned_data["name"],
                description=form.cleaned_data["description"],                       #descripcion 
                price=form.cleaned_data["price"],                                   #precio
                stock=form.cleaned_data["stock"],                                   #stock
                image=form.cleaned_data["image"],                                   #imagen
                brand=form.cleaned_data["brand"]                                    #marca                
            )
            return redirect(list_products)

     elif request.method=="GET":                                                    
        form=Formulario_productos()
        context={"form":form}
        return render(request,"new_product.html",context=context)
    
    else:
        return redirect (list_products)


def list_products(request):                                                         #funcion para mostrar todos los productos
    products= Products.objects.all()
    context={"products":products}
    return render(request,"products_list.html",context=context)

def list_products_highest(request):                                                 #funcion que ordena por precio
    products= Products.objects.all().order_by("-price")
    context={"products":products}
    return render(request,"products_list_highest.html",context=context)

def list_products_lowest(request):                                                  #funcion que ordena por precio
    products= Products.objects.all().order_by("price")
    context={"products":products}
    return render(request,"products_list_lowest.html",context=context)

   

@login_required
def update_product(request, pk):                                                    #funcion para actualizar informacion del profucto
    if request.user.is_superuser:
     if request.method=="POST":
        form=Formulario_productos(request.POST,request.FILES)
        if form.is_valid():
            product= Products.objects.get(id=pk)
            product.name=form.cleaned_data["name"]
            product.description=form.cleaned_data["description"]              
            product.price=form.cleaned_data["price"]
            product.stock=form.cleaned_data["stock"]  
            product.brand=form.cleaned_data["brand"] 
            product.image=form.cleaned_data["image"] 
            product.save()

            return redirect(list_products) 
                             
            
     elif request.method=="GET":                                                   
        product=Products.objects.get(id=pk)
        form=Formulario_productos(initial={
            "name":product.name,
            "price":product.price,
            "description":product.description,
            "stock":product.stock,
            "image":product.image,
            "brand":product.brand})
        context={"form":form}
        return render(request,"update_product.html",context=context)
    else:
        return redirect (list_products)

def search_products(request):                                                           #funcion para buscar profucto
    search=request.GET["search"]
    products=Products.objects.filter(name__icontains=search)
    context={"products":products}
    return render(request,"search_product.html",context=context)



def remove_product(request, id):                                                        #funcion borrar producto
    if request.user.is_superuser:
     if request.method == 'GET':
        product = Products.objects.get(id=id)
        context = {'product':product}
        return render(request, 'remove_product.html', context=context)
     elif request.method == 'POST':
        product = Products.objects.get(id=id)
        product.delete()
        return redirect(list_products)
    
    else:
        return redirect (list_products)


def descripction_product(request, id):                                                  #funcion de muestra de informacion del producto
    if request.method == 'GET':
        product = Products.objects.get(id=id)
        context = {'product':product}
        return render(request, 'detalles.html', context=context)

@login_required
def store(request):                                                                     #funcion carrito       
    products= Products.objects.all()
    return render(request,"store.html",{'products':products})

def add_product(request,product_id):                                                    #funcion añadir al carrito 
    cart=Cart(request)  
    product=Products.objects.get(id=product_id)
    cart.add(product)
    return redirect(store)

def delete_product(request,product_id):                                                 #funcion borrar del carrito 
    cart=Cart(request)
    product=Products.objects.get(id=product_id)
    cart.delete(product)
    return redirect(store)

def subtract_product(request,product_id):                                               #funcion restar del carrito 
    cart=Cart(request)
    product=Products.objects.get(id=product_id)
    cart.subtract(product)
    return redirect(store)

def clean_cart(request):                                                                #funcion vaciar carrito 
    cart=Cart(request)
    cart.clean()
    return redirect(store)



    

