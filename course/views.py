from django.shortcuts import render

# Create your views here.


def home (request):
    return render(request, 'course/index.html')

def loginPage (request):
    return render(request, 'course/login.html')


def shortTermCourseCreate (request):
    return render(request, 'course/short-course-create.html')

def shortTermCourseView (request):
    return render(request, 'course/short-course-view.html')

def userProfile (request):
    return render(request, 'course/profile.html')