from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from accounts.models import User
from accounts.forms import UserForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import logout,authenticate,login

# Create your views here.

@login_required(login_url='login-page')
def home (request):
    
    return render(request, 'course/index.html')

def login_Page (request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method =='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if not User.objects.filter(email=email).exists():
            messages.error(request, "Invalid Email Adress")
            return redirect('login-page')
        
        if not User.objects.filter(email=email,is_active=True).exists():
            messages.error(request, "You are blocked by admin ! Please contact admin")
            return redirect('login-page')
        
        
        user = authenticate(username=email,password=password)
        if user is None:
            messages.error(request, "Invalid Password")
            return redirect('login-page')
        else:
            messages.success(request, f'Welcome Back {user.first_name}')
            login(request,user)
            return redirect('home')
        
    return render(request, 'course/login.html')


class register_Page(CreateView):
    model = User
    form_class = UserForm
    template_name = 'course/register.html'
    success_url = reverse_lazy('login-page')
    
    def form_valid(self, form):
        messages.success(self.request, 'Registration successful. You can now log in.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Registration failed. Please correct the errors')
        return super().form_invalid(form)
    

def logout_Page(request):
    logout(request)
    return redirect('login-page')
    

@login_required(login_url='login-page')
def shortTermCourseCreate (request):
    return render(request, 'course/short-course-create.html')


@login_required(login_url='login-page')
def shortTermCourseView (request):
    return render(request, 'course/short-course-view.html')


@login_required(login_url='login-page')
def userProfile (request):
    return render(request, 'course/profile.html')