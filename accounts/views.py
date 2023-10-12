from django.shortcuts import render
from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash
import json
from django.http import JsonResponse
from .models import User
from django.contrib import messages
# Create your views here.

#change password with old password
def change_user_password_with_oldpass(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if request.method == "POST" and is_ajax:
        data = json.load(request)
                
        try:
            current_password= request.user.password #user's current password
            current_password_entered= data['old_password']
            password2= data['password2']

            matchcheck= check_password(current_password_entered, current_password)
            
            if matchcheck:
                user = User.objects.get(id=request.user.id)
                user.set_password(password2)
                user.save()  
                update_session_auth_hash(request, user)

                messages.success(request, "Password Change Successfully")
                return JsonResponse({"status": "success"})
            else:
                return JsonResponse({"status": "error","message": "Invalid Old Password"})
        
        except Exception as e:
            print(e)
            return JsonResponse({"status": "error", "message": "Contact Admin"})

    else:
        # Return a JSON response indicating an invalid request
        return JsonResponse({"status": "error", "message": "Invalid request"})