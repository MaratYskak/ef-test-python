from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import AuthToken
from users.serializers import (
    LoginSerializer,
    RegisterSerializer,
)


class RegisterView(APIView):

    authentication_classes = []
    permission_classes = []

    def post(self, request):

        serializer = RegisterSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        user = serializer.save()

        return Response(
            {
                'message': 'User created successfully',
                'user_id': user.id,
            },
            status=status.HTTP_201_CREATED
        )


class LoginView(APIView):

    authentication_classes = []
    permission_classes = []

    def post(self, request):

        serializer = LoginSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']

        password = serializer.validated_data['password']

        user = authenticate(
            request,
            email=email,
            password=password
        )

        if not user:
            return Response(
                {
                    'detail': 'Invalid credentials'
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

        if not user.is_active:
            return Response(
                {
                    'detail': 'User is inactive'
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

        token = AuthToken.objects.create(
            user=user
        )

        return Response(
            {
                'token': token.key
            },
            status=status.HTTP_200_OK
        )
    
class ProfileView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        return Response(
            {
                'id': request.user.id,
                'email': request.user.email,
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
            }
        )
    
class LogoutView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        request.auth.delete()

        return Response(
            {
                'message': 'Logged out successfully'
            },
            status=status.HTTP_200_OK
        )
    
class SoftDeleteUserView(APIView):

    permission_classes = [IsAuthenticated]

    def delete(self, request):

        user = request.user

        user.is_active = False

        user.save()

        user.tokens.all().delete()

        return Response(
            {
                'message': 'User soft deleted'
            },
            status=status.HTTP_200_OK
        )