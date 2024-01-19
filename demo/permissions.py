# permissions.py
from rest_framework import permissions

class IsAdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        print('req', request.authorization)
        if request.authorization != None:
            return True
        return False
