from django.urls import path, include
from .views import (
            Student, TeacherStudent, 
            UsersRegister, StudentProfileView,
)

urlpatterns = [
    path('register', UsersRegister.as_view()), # to register new users of different types
    path('students', Student.as_view()),   #to register new students which can we accesed by the teachers 
    path('teacherstudent', TeacherStudent.as_view()), #to register new students and teachers which can we accesed by the admin 
    path('studentprofile', StudentProfileView.as_view()), # to view student profile by students
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')), # to reset password
]
