from django.contrib import admin
from django.urls import path, include 
from products.views import inicio 

urlpatterns = [
    path('admin/', admin.site.urls),
    path("products/",include("products.urls")),
    path("products/",inicio,name="inicio")
]