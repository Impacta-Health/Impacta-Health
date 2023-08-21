from django.db import models
from django_cleanup import cleanup
from users import enums
from django.conf import settings
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from users.validator.custom_password import validate_username


class User(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=30, validators=[validate_username], unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_type = models.CharField(max_length=7,choices=enums.UserTypeEnum.choices,)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    report = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    REQUIRED_FIELDS = ["first_name", "last_name", "user_type"]

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        ordering = ["id"]
