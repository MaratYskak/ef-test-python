from django.core.management.base import BaseCommand

from access.models import (
    Action,
    Permission,
    Resource,
    Role,
)


class Command(BaseCommand):

    help = 'Seed RBAC test data'

    def handle(self, *args, **kwargs):

        admin_role, _ = Role.objects.get_or_create(
            name='admin'
        )

        manager_role, _ = Role.objects.get_or_create(
            name='manager'
        )

        user_role, _ = Role.objects.get_or_create(
            name='user'
        )

        users_resource, _ = Resource.objects.get_or_create(
            name='users'
        )

        reports_resource, _ = Resource.objects.get_or_create(
            name='reports'
        )

        analytics_resource, _ = Resource.objects.get_or_create(
            name='analytics'
        )

        create_action, _ = Action.objects.get_or_create(
            name='create'
        )

        read_action, _ = Action.objects.get_or_create(
            name='read'
        )

        update_action, _ = Action.objects.get_or_create(
            name='update'
        )

        delete_action, _ = Action.objects.get_or_create(
            name='delete'
        )

        resources = [
            users_resource,
            reports_resource,
            analytics_resource,
        ]

        actions = [
            create_action,
            read_action,
            update_action,
            delete_action,
        ]

        for resource in resources:
            for action in actions:
                Permission.objects.get_or_create(
                    role=admin_role,
                    resource=resource,
                    action=action
                )

        Permission.objects.get_or_create(
            role=manager_role,
            resource=reports_resource,
            action=read_action
        )

        Permission.objects.get_or_create(
            role=manager_role,
            resource=reports_resource,
            action=update_action
        )

        Permission.objects.get_or_create(
            role=manager_role,
            resource=analytics_resource,
            action=read_action
        )

        Permission.objects.get_or_create(
            role=user_role,
            resource=analytics_resource,
            action=read_action
        )

        self.stdout.write(
            self.style.SUCCESS(
                'RBAC data seeded successfully'
            )
        )