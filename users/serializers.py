from rest_framework import serializers

from users.models import User


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        min_length=6
    )

    password_confirm = serializers.CharField(
        write_only=True
    )

    class Meta:
        model = User

        fields = (
            'email',
            'password',
            'password_confirm',
            'first_name',
            'last_name',
            'middle_name',
        )

    def validate(self, attrs):

        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError(
                'Passwords do not match'
            )

        return attrs

    def create(self, validated_data):

        validated_data.pop('password_confirm')

        password = validated_data.pop('password')

        user = User.objects.create_user(
            password=password,
            **validated_data
        )

        return user


class LoginSerializer(serializers.Serializer):

    email = serializers.EmailField()

    password = serializers.CharField()