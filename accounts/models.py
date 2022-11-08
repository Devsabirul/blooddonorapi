from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import *


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    is_admin = models.BooleanField('Is admin', default=False)
    is_donor = models.BooleanField('Is donor', default=False)
    is_available = models.BooleanField(
        'Is available', default=False, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
