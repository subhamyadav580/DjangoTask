from .permissions import IsTeacher, IsAdmin, IsStudent
from .models import User, StudentProfile
from .serializers import (
    RegisterSerializer, RegisterStudentSerializer, 
    StudentsSerializers, RegisterTeacherStudentSerializer,
    TeacherStudentSerializers
    )
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UsersRegister(APIView):

    """
    Class for creating different users.
    """

    def post(self, request, format=None):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class Student(APIView):

    permission_classes = [IsTeacher]

    def get(self, request, format=None):
        """
        List all Students by teachers only
        """
        users_list = User.objects.filter(is_student=True)
        serializer = StudentsSerializers(users_list, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Add new students by teachers only.
        """
        serializer = RegisterStudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TeacherStudent(APIView):

    permission_classes = [IsAdmin]

    def get(self, request, format=None):
        """
        List all Students and Teachers by admin only
        """
        users_list = User.objects.filter(is_admin=False)
        serializer = TeacherStudentSerializers(users_list, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Add new Students and Teachers by admin only
        """
        serializer = RegisterTeacherStudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentProfileView(APIView):

    """
    To view the students profile which can be only accesed by students
    """

    permission_classes = [IsStudent]

    def get(self, request, format=None):
        userProfile = StudentProfile.objects.get(user=request.user)
        data = {
            "username" : userProfile.user.username,
            "Email" : userProfile.user.email,
            "First Name" : userProfile.user.first_name,
            "Last Name" : userProfile.user.last_name,
            "Middle Name" : userProfile.user.middle_name,
            "is_student" : userProfile.user.is_student,
            
        }
        return Response(data)
