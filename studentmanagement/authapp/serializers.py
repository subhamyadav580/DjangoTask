import email
from email import utils
from lib2to3.pgen2 import token
from re import I
from turtle import st
from urllib import request
from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 
                        'first_name', 'middle_name', 'last_name', 
                        'is_admin', 'is_teacher', 'is_student')


    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name = validated_data['first_name'],
            middle_name = validated_data['middle_name'],
            last_name = validated_data['last_name'],
            is_admin=validated_data['is_admin'],
            is_teacher=validated_data['is_teacher'],
            is_student=validated_data['is_student'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

class StudentsSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'is_admin', 'is_teacher', 'is_student')
  

class RegisterStudentSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 
                    'first_name', 'middle_name', 'last_name',  
                    'is_student')

        
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        print(attrs['is_student'])
        if attrs['is_student'] != True:
            raise serializers.ValidationError({"is_student": "Student fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name = validated_data['first_name'],
            middle_name = validated_data['middle_name'],
            last_name = validated_data['last_name'],
            is_student=validated_data['is_student'],
        )

        user.set_password(validated_data['password'])
        user.save()
        return user


class TeacherStudentSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'is_admin', 'is_teacher', 'is_student')
  

class RegisterTeacherStudentSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 
                    'email', 'first_name', 'middle_name', 
                    'last_name', 'is_student', 'is_teacher')

        
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name = validated_data['first_name'],
            middle_name = validated_data['middle_name'],
            last_name = validated_data['last_name'],
            is_student=validated_data['is_student'],
            is_teacher=validated_data['is_teacher'],
        )

        user.set_password(validated_data['password'])
        user.save()
        return user


