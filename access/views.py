from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from access.permissions import HasPermission


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