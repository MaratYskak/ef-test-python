from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from access.permissions import HasPermission

from access.admin_permissions import IsAdminRole

from access.models import (
    Permission,
    Role,
    UserRole,
)

from access.serializers import (
    AssignRoleSerializer,
    PermissionSerializer,
    RoleSerializer,
)


class AnalyticsView(APIView):

    permission_classes = [
        IsAuthenticated,
        HasPermission
    ]

    required_resource = 'analytics'

    required_action = 'read'

    def get(self, request):

        return Response(
            {
                'analytics': [
                    'sales report',
                    'users activity',
                    'conversion stats',
                ]
            }
        )


class ReportsView(APIView):

    permission_classes = [
        IsAuthenticated,
        HasPermission
    ]

    required_resource = 'reports'

    required_action = 'read'

    def get(self, request):

        return Response(
            {
                'reports': [
                    'monthly report',
                    'finance report',
                ]
            }
        )


class UsersDeleteView(APIView):

    permission_classes = [
        IsAuthenticated,
        HasPermission
    ]

    required_resource = 'users'

    required_action = 'delete'

    def delete(self, request):

        return Response(
            {
                'message': 'User deleted'
            }
        )
    
class RolesListView(APIView):

    permission_classes = [
        IsAuthenticated,
        IsAdminRole,
    ]

    def get(self, request):

        roles = Role.objects.all()

        serializer = RoleSerializer(
            roles,
            many=True
        )

        return Response(serializer.data)


class PermissionsListView(APIView):

    permission_classes = [
        IsAuthenticated,
        IsAdminRole,
    ]

    def get(self, request):

        permissions = Permission.objects.select_related(
            'role',
            'resource',
            'action'
        ).all()

        serializer = PermissionSerializer(
            permissions,
            many=True
        )

        return Response(serializer.data)


class AssignRoleView(APIView):

    permission_classes = [
        IsAuthenticated,
        IsAdminRole,
    ]

    def post(self, request):

        serializer = AssignRoleSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        user_role = UserRole.objects.create(
            user_id=serializer.validated_data['user_id'],
            role_id=serializer.validated_data['role_id'],
        )

        return Response(
            {
                'message': 'Role assigned',
                'user_role_id': user_role.id,
            }
        )