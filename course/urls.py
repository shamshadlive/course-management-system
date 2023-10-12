from django.urls import path
from .views import home,loginPage,shortTermCourseView,shortTermCourseCreate,userProfile

urlpatterns = [
    path("", home, name="home"),
    path("login/", loginPage, name="login-page"),
    path("shorterm-course/", shortTermCourseView, name="short-term-course"),
    path("shorterm-course/create/", shortTermCourseCreate, name="short-term-course-create"),
    path("profile/", userProfile, name="user-profile"),
    ]