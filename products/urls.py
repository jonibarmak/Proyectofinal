from turtle import home
from django.urls import path
from products.views import list_products, create_product,search_products,descripction_product,remove_product,update_product
from .views import add_product, delete_product, clean_cart, subtract_product, store,list_products_highest,list_products_lowest  

urlpatterns = [
    path("create_product/",create_product,name="create_product"),                           #link para crear producto
    path("list-products/",list_products,name="list-products"),                              #link para mostrar lista de productos
    path("list-products-highest/",list_products_highest,name="list-products-highest"),      #link para mostrar los productos ordenados por valor    
    path("list-products-lowest/",list_products_lowest,name="list-products-lowest"),         #link para mostrar los productos ordenados por valor 
    path("search-products/",search_products,name="search-products"),                        #link para buscar producto
    path("detalles/<int:id>/",descripction_product,name="descripction_product" ),           #link para mostrar descripcion de producto
    path("remove-product/<int:id>/",remove_product,name="remove-product" ),                 #link para borrar producto del sv
    path("update-product/<int:pk>/",update_product,name="update-product"),                  #link para cambiar info del producto
    path("store/",store,name="store"),                                                      #link para comprar y añadir al carrito  
    path('add-product/<int:product_id>/', add_product, name='Add'),                         #link para sumar un producto al carrito
    path('delete-product/<int:product_id>/', delete_product, name='Del'),                   #link para borrar del carrito
    path('subtract-product/<int:product_id>/', subtract_product, name='Sub'),               #link para restar un producto al carrito
    path('clean-cart/', clean_cart, name='CLS'),                                            #link para limpiar carrito

   
]
