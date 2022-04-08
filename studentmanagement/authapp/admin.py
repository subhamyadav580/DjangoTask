from django.contrib import admin
from .models import StudentProfile, User

class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ("username", "email", 'is_student', 'is_teacher', 'is_admin', )



class StudentProfileAdmin(admin.ModelAdmin):
    model = StudentProfile
    list_display = ("username", "email", "full_name", 'is_student', )

    def username(self, obj):
        return obj.user
        
    def email(self, obj):
        return obj.user.email

    def full_name(self, obj):
        return f'{obj.user.first_name} {obj.user.middle_name} {obj.user.last_name}'
    
    def is_student(self, obj):
        return f'{obj.user.is_student}'


admin.site.register(User, UserAdmin)
admin.site.register(StudentProfile, StudentProfileAdmin)
