from django.urls import path
from products.views import list_products,create_product, primer_formulario

urlpatterns = [
    path("list-products/",list_products,name="list-products"),
    path("create_product/",create_product,name="create_product"),
    path("primer-formulario/",primer_formulario,name="primer-formulario"),

]