from django.db.models import TextChoices

class UserTypeEnum(TextChoices):
    ADMIN = "admin"
    PATIENT = "patient"
    DOCTOR = "doctor"

