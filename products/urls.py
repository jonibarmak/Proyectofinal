from django.urls import path
from products.views import list_products, create_product,search_products,descripction_product,borrar_producto,update_product,tienda
from .views import agregar_producto, eliminar_producto, limpiar_carrito, restar_producto

urlpatterns = [
    path("create_product/",create_product,name="create_product"),
    path("list-products/",list_products,name="list-products"),
    path("search-products/",search_products,name="search-products"),
    path("detalles/<int:id>/",descripction_product,name="descripction_product" ),
    path("borrar/<int:id>/",borrar_producto,name="borrar_producto" ),
    path("update-product/<int:pk>/",update_product,name="update-product"),
    path("tienda/",tienda,name="tienda"),
    path('agregar/<int:product_id>/', agregar_producto, name='Add'),
    path('eliminar/<int:product_id>/', eliminar_producto, name='Del'),
    path('restar/<int:product_id>/', restar_producto, name='Sub'),
    path('limpiar/', limpiar_carrito, name='CLS'),
   
]