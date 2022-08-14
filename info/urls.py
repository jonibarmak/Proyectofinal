from django.urls import path
from info.views import route_about, list_us

urlpatterns = [
    path("route_about/",route_about,name="route_about"),
    path("list_us/",list_us,name="list_us"),
    
   
]