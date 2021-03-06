from rest_framework import permissions


class IsTeacher(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_teacher:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_teacher:
            return True
        return False


class IsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_admin:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_admin:
            return True
        return False

class IsStudent(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_student:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_student:
            return True
        return False
        