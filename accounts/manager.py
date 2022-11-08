from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
'''

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        user = self.model(email=email, **extra_fields)
        user.set_password(user.password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_admin', True)
        return self.create_user(email, password, **extra_fields)

'''


class UserManager(BaseUserManager):
    def create_user(self, email, is_admin, is_donor, is_available, password=None, password2=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email), is_admin=is_admin,
                          is_donor=is_donor, is_available=is_available, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, password2=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_admin', True)
        return self.create_user(email, password, password2, **extra_fields)
