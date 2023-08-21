from django.contrib.auth.models import BaseUserManager
from django.db import models


class UserManager(BaseUserManager, models.Manager):
    def get_by_natural_key(self, username):
        return self.get(username=username)

class UserProfileManager(models.Manager):
    def get_by_natural_key(self, user):
        return self.get(user=user)