from django.urls import path
from access.views import (
    RolesListView,
    PermissionsListView,
    AssignRoleView,
    AnalyticsView,
    ReportsView,
    UsersDeleteView,
)

urlpatterns = [
    # business endpoints
    path('analytics/', AnalyticsView.as_view()),
    path('reports/', ReportsView.as_view()),
    path('users/delete/', UsersDeleteView.as_view()),

    # admin endpoints
    path('admin/roles/', RolesListView.as_view()),
    path('admin/permissions/', PermissionsListView.as_view()),
    path('admin/assign-role/', AssignRoleView.as_view()),
]