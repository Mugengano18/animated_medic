from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from .manager import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=12, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.phone_number