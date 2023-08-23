from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.db.models.query import QuerySet
from django.utils.translation import gettext_lazy as _

from users.enums import UserRole


class UserManager(BaseUserManager, models.Manager):
    def create_superuser(self, email, username, first_name, password, **other_fields):
        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to is_staff=True.")
        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be assigned to is_superuser=True.")

        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        return self.create_user(email, username, first_name, password, **other_fields)

    def create_user(self, email, username, first_name, password, **other_fields):
        if not email:
            raise ValueError(_("Email must be provide."))

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            first_name=first_name,
            **other_fields,
        )
        user.set_password(password)
        user.save()
        return user

    def get_by_natural_key(self, username):
        return self.get(username=username)


class AdminUserManager(BaseUserManager, models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(role=UserRole.ADMIN)

    def get_by_natural_key(self, username):
        return self.get(username=username)


class DoctorUserManager(BaseUserManager, models.Manager):
    def get_queryset(self, *args, **kwargs) -> QuerySet:
        return super().get_queryset().filter(role=UserRole.DOCTOR)

    def get_by_natural_key(self, username):
        return self.get(username=username)


class PatientUserManager(BaseUserManager, models.Manager):
    def get_queryset(self, *args, **kwargs) -> QuerySet:
        return super().get_queryset().filter(role=UserRole.PATIENT)

    def get_by_natural_key(self, username):
        return self.get(username=username)


class UserProfileManager(models.Manager):
    def get_by_natural_key(self, user):
        return self.get(user=user)
