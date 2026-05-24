from rest_framework import serializers

from access.models import (
    Permission,
    Role,
    UserRole,
)


class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role

        fields = '__all__'


class PermissionSerializer(serializers.ModelSerializer):

    role = serializers.StringRelatedField()

    resource = serializers.StringRelatedField()

    action = serializers.StringRelatedField()

    class Meta:
        model = Permission

        fields = '__all__'


class AssignRoleSerializer(serializers.Serializer):

    user_id = serializers.IntegerField()

    role_id = serializers.IntegerField()

    def validate(self, attrs):

        user_id = attrs['user_id']

        role_id = attrs['role_id']

        if UserRole.objects.filter(
            user_id=user_id,
            role_id=role_id
        ).exists():
            raise serializers.ValidationError(
                'Role already assigned'
            )

        return attrs