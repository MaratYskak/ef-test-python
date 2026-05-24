from rest_framework.permissions import BasePermission


class IsAdminRole(BasePermission):

    message = 'Admin role required'

    def has_permission(self, request, view):

        user = request.user

        if not user.is_authenticated:
            return False

        return user.user_roles.filter(
            role__name='admin'
        ).exists()