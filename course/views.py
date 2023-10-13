from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from accounts.models import User
from accounts.forms import UserForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import logout,authenticate,login
from .models import ShortTermCourse
from .forms import ShortTermCourseUpdateForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from django.http import JsonResponse
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


class shortTermCourse_Create(LoginRequiredMixin,CreateView):
    model = ShortTermCourse
    form_class = ShortTermCourseUpdateForm
    template_name = 'course/short-course-create.html'
    success_url = reverse_lazy('short-term-course')


    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, f'{form.instance.title} Created Succesfully !')
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, 'Invalid Form Please correct the errors')
        return super().form_invalid(form)
    
class ShortTermCourseUpdate(LoginRequiredMixin,UpdateView):
    model = ShortTermCourse
    form_class = ShortTermCourseUpdateForm
    template_name = 'course/short-course-create.html' 
    success_url = reverse_lazy('short-term-course')
    
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, f'{form.instance.title} Created Succesfully !')
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, 'Invalid Form Please correct the errors')
        return super().form_invalid(form)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['description_content'] = self.object.description  
        return context
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user == self.request.user:
            return obj
        else:
            raise Http404("You have no permssion to view")
        
@login_required
def delete_short_term_course(request, pk):
    course = get_object_or_404(ShortTermCourse, pk=pk)
    
    if course.user == request.user:
        course.delete()
        messages.success(request, f'{course.title} Deleted Successfully!')
        return redirect('short-term-course')
    else:
        return HttpResponseForbidden("You are not allowed to delete this course")
    
    
class shortTermCourseView(ListView):
    model = ShortTermCourse
    template_name = 'course/short-course-view.html'  
    context_object_name = 'courses'  
    paginate_by = 12  

    def get_queryset(self):
        queryset = ShortTermCourse.objects.filter(user=self.request.user).order_by('-updated_at')
        search_query = self.request.GET.get('search', None)
        if search_query:
            # Filter the queryset based on the search query
            queryset = queryset.filter(Q(title__icontains=search_query) 
                                              | Q(subtitle__icontains=search_query)
                                               | Q(description__icontains=search_query)
                                               
                                               )
        
        return queryset
    


@login_required(login_url='login-page')
def userProfile (request):
    return render(request, 'course/profile.html')



def autocomplete(request):
    try:
        if 'term' in request.GET:
            search_query = request.GET.get('term')
            short_term_course = ShortTermCourse.objects.filter(user=request.user)
            
            #search
            terms = search_query.split()  # Split the search query into individual terms
            for term in terms:
                short_term_course = [
                                course for course in short_term_course
                                if term.lower() in course.course_name().lower()
                            ]
            
            title = []
            title += [ x.course_name() for x in short_term_course ]
            return JsonResponse(title,safe=False)
    except:
        return JsonResponse({
            'status':400
        })
        