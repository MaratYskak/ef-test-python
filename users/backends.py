from django.contrib.auth.backends import BaseBackend

from users.models import User


class EmailAuthBackend(BaseBackend):

    def authenticate(
        self,
        request,
        email=None,
        password=None,
        **kwargs
    ):

        if not email or not password:
            return None

        try:
            user = User.objects.get(email=email)

        except User.DoesNotExist:
            return None

        if not user.check_password(password):
            return None

        if not user.is_active:
            return None

        return user

    def get_user(self, user_id):

        try:
            return User.objects.get(id=user_id)

        except User.DoesNotExist:
            return None