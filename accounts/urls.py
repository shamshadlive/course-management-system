from django.urls import path
from .views import change_user_password_with_oldpass

urlpatterns = [
    path("users/basic/changepassword", change_user_password_with_oldpass, name="user-change-password"),
    
    ]