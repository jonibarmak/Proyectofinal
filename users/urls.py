from django.urls import path
from users.views import login_request, register, show_profile, create_profile, update_profile,descripction_profile
from django.contrib.auth.views import LogoutView 


urlpatterns = [
    path("login/",login_request,name="login"),
    path("register/",register,name="register"),
    path("logout/",LogoutView.as_view(template_name="logout.html"),name="logout"),
    path("profile/",show_profile,name="profile"),
    path("create-profile/",create_profile,name="create-profile"),
    path("update-profile/",update_profile,name="update-profile"),
    path("detalles_perfil/",descripction_profile,name="detalles_perfil"),
    
    

]