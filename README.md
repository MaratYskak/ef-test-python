# Custom Authentication & Authorization System

Backend application built with Django REST Framework and PostgreSQL.

The project implements a custom authentication and authorization system with Role-Based Access Control (RBAC).

---

# Technologies

- Python
- Django
- Django REST Framework
- PostgreSQL

---

# Features

## Authentication

- User registration
- Login by email and password
- Custom token authentication
- Logout
- Soft delete users

## Authorization

Custom RBAC system with:

- Roles
- Resources
- Actions
- Permissions

Users receive access to resources through assigned roles.

---

# RBAC Architecture

## Entities

### User

System user authenticated by email/password.

### Role

Represents a user role.

Examples:

- admin
- manager
- user

### Resource

Represents protected business resources.

Examples:

- users
- reports
- analytics

### Action

Represents allowed operation.

Examples:

- create
- read
- update
- delete

### Permission

Defines access rule:

Role + Resource + Action

Example:

admin + users + delete

### UserRole

Many-to-many relation between users and roles.

---

# Authentication Flow

1. User logs in with email/password
2. System validates credentials
3. Auth token is generated
4. Client sends token in Authorization header

Example:

Authorization: Token your_token

---

# Authorization Flow

1. Request is authenticated
2. System identifies user roles
3. Permission class checks required:
   - resource
   - action
4. Access granted or denied

---

# API Endpoints

## Authentication

### Register

POST /api/users/register/

### Login

POST /api/users/login/

### Profile

GET /api/users/profile/

### Logout

POST /api/users/logout/

### Soft Delete User

DELETE /api/users/delete/

---

## RBAC Business Resources

### Analytics

GET /api/access/analytics/

### Reports

GET /api/access/reports/

### Users Delete

DELETE /api/access/users/delete/

---

## Admin RBAC API

### Roles List

GET /api/access/admin/roles/

### Permissions List

GET /api/access/admin/permissions/

### Assign Role

POST /api/access/admin/assign-role/

---

# Setup

## Install dependencies

```bash
pip install -r requirements.txt
```

## Configure environment

Create `.env` file:

```env
SECRET_KEY=your_secret_key

DB_NAME=custom_auth_db
DB_USER=custom_auth_user
DB_PASSWORD=strong_password
DB_HOST=localhost
DB_PORT=5432
```

## Run migrations

```bash
python manage.py migrate
```

## Seed RBAC data

```bash
python manage.py seed_rbac
```

## Run server

```bash
python manage.py runserver
```

---

# HTTP Status Codes

- 200 OK
- 201 Created
- 401 Unauthorized
- 403 Forbidden

---

# Notes

The project intentionally implements a custom authentication and authorization system instead of relying completely on Django built-in permissions system.
