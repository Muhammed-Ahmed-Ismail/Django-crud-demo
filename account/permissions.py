from rest_framework.permissions import BasePermission


class UserIsDeveloper(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='developer').exists():
            return True
        return False
