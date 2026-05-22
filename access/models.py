from django.conf import settings
from django.db import models


class Role(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name


class Resource(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True
    )

    def __str__(self):
        return self.name


class Action(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True
    )

    def __str__(self):
        return self.name


class Permission(models.Model):

    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        related_name='permissions'
    )

    resource = models.ForeignKey(
        Resource,
        on_delete=models.CASCADE
    )

    action = models.ForeignKey(
        Action,
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = (
            'role',
            'resource',
            'action'
        )

    def __str__(self):
        return (
            f'{self.role.name} - '
            f'{self.resource.name} - '
            f'{self.action.name}'
        )


class UserRole(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user_roles'
    )

    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        related_name='user_roles'
    )

    assigned_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        unique_together = (
            'user',
            'role'
        )

    def __str__(self):
        return f'{self.user.email} - {self.role.name}'