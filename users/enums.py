from django.db import models


class UserRole(models.TextChoices):
    ADMIN = "Admin"
    DOCTOR = "Doctor"
    PATIENT = "Patient"
