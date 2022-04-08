from django.urls import path
from .views import (
            Student, TeacherStudent, 
            UsersRegister, StudentProfileView
)


urlpatterns = [
    path('register', UsersRegister.as_view()),
    path('students', Student.as_view()),  
    path('teacherstudent', TeacherStudent.as_view()),
    path('studentprofile', StudentProfileView.as_view()),
]
