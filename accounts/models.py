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
