from rest_framework.permissions import BasePermission



class IsClientUser(BasePermission):
    def has_permission(self, request, view):

        return bool(request.user and request.user.is_client)


class IsFreelanceUser(BasePermission):
    def has_permission(self, request, view):

        return bool(request.user and request.user.is_freecancer)