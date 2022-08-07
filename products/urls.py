from django.urls import path
from products.views import list_products, create_product, primer_formulario,search_products,descripction_product,borrar_producto

urlpatterns = [
    path("create_product/",create_product,name="create_product"),
    path("list-products/",list_products,name="list-products"),
    path("primer-formulario/",primer_formulario,name="primer-formulario"),
    path("search-products/",search_products,name="search-products"),
    path("detalles/<int:id>/",descripction_product,name="descripction_product" ),
    path("borrar/<int:id>/",borrar_producto,name="borrar_producto" ),
   
]