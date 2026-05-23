from django.urls import path
from users.views import LogoutView, ProfileView, SoftDeleteUserView

from users.views import (
    LoginView,
    ProfileView,
    RegisterView,
)

urlpatterns = [
    path(
        'register/',
        RegisterView.as_view(),
        name='register'
    ),

    path(
        'login/',
        LoginView.as_view(),
        name='login'
    ),

    path(
        'profile/',
        ProfileView.as_view(),
        name='profile'
    ),

    path(
        'logout/',
        LogoutView.as_view(),
        name='logout'
    ),
    
    path(
        'soft-delete/',
        SoftDeleteUserView.as_view(),
        name='soft-delete'
    ),
]