from rest_framework.authentication import (
    BaseAuthentication,
)
from rest_framework.exceptions import AuthenticationFailed

from users.models import AuthToken


class CustomTokenAuthentication(BaseAuthentication):

    keyword = 'Token'

    def authenticate(self, request):

        auth_header = request.headers.get(
            'Authorization'
        )

        if not auth_header:
            return None

        parts = auth_header.split()

        if len(parts) != 2:
            raise AuthenticationFailed(
                'Invalid token header'
            )

        keyword, token = parts

        if keyword != self.keyword:
            raise AuthenticationFailed(
                'Invalid token prefix'
            )

        try:
            auth_token = AuthToken.objects.select_related(
                'user'
            ).get(key=token)

        except AuthToken.DoesNotExist:
            raise AuthenticationFailed(
                'Invalid token'
            )

        user = auth_token.user

        if not user.is_active:
            raise AuthenticationFailed(
                'User inactive'
            )

        return (user, auth_token)