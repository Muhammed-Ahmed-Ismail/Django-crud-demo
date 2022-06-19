from rest_framework.permissions import BasePermission


class CheckDevGroup(BasePermission):
    def has_permission(self, request, view):
        print('inside permission')
        for grp in request.user.groups.all():
            print("group", grp)

        if request.user.groups.filter(name='Developer').exists():
            return True
        return False
