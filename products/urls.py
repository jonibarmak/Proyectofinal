from django.urls import path
from products.views import list_products, create_product,search_products,descripction_product,borrar_producto,update_product

urlpatterns = [
    path("create_product/",create_product,name="create_product"),
    path("list-products/",list_products,name="list-products"),
    path("search-products/",search_products,name="search-products"),
    path("detalles/<int:id>/",descripction_product,name="descripction_product" ),
    path("borrar/<int:id>/",borrar_producto,name="borrar_producto" ),
    path("update-product/<int:pk>/",update_product,name="update-product"),
   
]