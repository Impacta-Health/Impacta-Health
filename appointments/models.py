from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Appointment(models.Model):
    patient = models.ForeignKey(
        User,
        related_name="appointments",
        on_delete=models.CASCADE
    )
    department = models.CharField(max_length=40)
    doctor = models.CharField(max_length=50)
    datetime = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

