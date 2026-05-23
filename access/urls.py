from django.urls import path

from access.views import (
    AnalyticsView,
    ReportsView,
    UsersDeleteView,
)

urlpatterns = [
    path(
        'analytics/',
        AnalyticsView.as_view(),
        name='analytics'
    ),

    path(
        'reports/',
        ReportsView.as_view(),
        name='reports'
    ),

    path(
        'users/delete/',
        UsersDeleteView.as_view(),
        name='users-delete'
    ),
]