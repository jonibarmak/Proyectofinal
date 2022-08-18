from django.urls import path
from products.views import list_products, create_product,search_products,descripction_product,remove_product,update_product
from .views import add_product, delete_product, clean_cart, subtract_product, store  

urlpatterns = [
    path("create_product/",create_product,name="create_product"),
    path("list-products/",list_products,name="list-products"),
    path("search-products/",search_products,name="search-products"),
    path("detalles/<int:id>/",descripction_product,name="descripction_product" ),
    path("remove-product/<int:id>/",remove_product,name="remove-product" ),
    path("update-product/<int:pk>/",update_product,name="update-product"),
    path("store/",store,name="store"),
    path('add-product/<int:product_id>/', add_product, name='Add'),
    path('delete-product/<int:product_id>/', delete_product, name='Del'),
    path('subtract-product/<int:product_id>/', subtract_product, name='Sub'),
    path('clean-cart/', clean_cart, name='CLS'),
   
]