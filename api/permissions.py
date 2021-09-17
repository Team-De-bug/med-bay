from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User


class IsDoctor(BasePermission):

    message = "you don't have permissions to access this"

    def has_permission(self, request, view):
        user = User.objects.get(username=request.user)
        return user.staff.role == 'd'


class IsPharma(BasePermission):

    message = "you don't have permissions to access this"

    def has_permission(self, request, view):
        user = User.objects.get(username=request.user)
        return user.staff.role == 'p'


class IsAdmin(BasePermission):

    message = "you don't have permissions to access this"

    def has_permission(self, request, view):
        user = User.objects.get(username=request.user)
        return user.staff.role == 'a'


class IsAccountant(BasePermission):

    message = "you don't have permissions to access this"

    def has_permission(self, request, view):
        user = User.objects.get(request.user)
        return user.staff.role == 'ac'
