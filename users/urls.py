from django.urls import path
from users.views import login_request, register,edit_profile,create_profile,delete_profile,show_profile
from django.contrib.auth.views import LogoutView 


urlpatterns = [
    path("login/",login_request,name="login"),
    path("register/",register,name="register"),
    path("logout/",LogoutView.as_view(template_name="logout.html"),name="logout"),
    path("profile/",show_profile,name="profile"),
    path("edit-profile//",edit_profile,name='edit-profile'),
    path("create-profile/",create_profile,name="create-profile"),
    path("delete-profile/",delete_profile,name='delete-profile'),
        
    
    

]