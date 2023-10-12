from django.urls import path
from .views import home,login_Page,shortTermCourseView,shortTermCourseCreate,userProfile,register_Page,logout_Page

urlpatterns = [
    path("", home, name="home"),
    path("login/", login_Page, name="login-page"),
    path("logout/", logout_Page, name="logout-page"),
    path("register/", register_Page.as_view(), name="register-page"),
    path("shorterm-course/", shortTermCourseView, name="short-term-course"),
    path("shorterm-course/create/", shortTermCourseCreate, name="short-term-course-create"),
    path("profile/", userProfile, name="user-profile"),
    ]