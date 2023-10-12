from django.urls import path
from .views import home,login_Page,shortTermCourseView,shortTermCourse_Create,userProfile,register_Page,logout_Page,ShortTermCourseUpdate,delete_short_term_course

urlpatterns = [
    path("", home, name="home"),
    path("login/", login_Page, name="login-page"),
    path("logout/", logout_Page, name="logout-page"),
    path("register/", register_Page.as_view(), name="register-page"),
    path("shorterm-course/", shortTermCourseView.as_view(), name="short-term-course"),
    path("shorterm-course/create/", shortTermCourse_Create.as_view(), name="short-term-course-create"),
    path("shorterm-course/<int:pk>/update/", ShortTermCourseUpdate.as_view(), name="short-term-course-update"),
    path("shorterm-course/<int:pk>/delete/", delete_short_term_course, name="short-term-course-delete"),
    path("profile/", userProfile, name="user-profile"),
    ]