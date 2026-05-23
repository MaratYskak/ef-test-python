from rest_framework.permissions import BasePermission

from access.models import Permission


class HasPermission(BasePermission):

    message = 'You do not have permission'

    def has_permission(self, request, view):

        required_resource = getattr(
            view,
            'required_resource',
            None
        )

        required_action = getattr(
            view,
            'required_action',
            None
        )

        if not required_resource or not required_action:
            return False

        user = request.user

        if not user.is_authenticated:
            return False

        user_roles = user.user_roles.select_related(
            'role'
        ).all()

        role_ids = [
            user_role.role.id
            for user_role in user_roles
        ]

        has_permission = Permission.objects.filter(
            role_id__in=role_ids,
            resource__name=required_resource,
            action__name=required_action,
        ).exists()

        return has_permission