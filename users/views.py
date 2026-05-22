from django.contrib.auth import authenticate

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