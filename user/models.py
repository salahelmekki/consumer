from django.db import models

# Create your models here.

from django.db import models
from .managers import UserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
import uuid


# models user details
class User(AbstractBaseUser, PermissionsMixin):
    CUSTOMER = "CUSTOMER"
    choice = [
        (CUSTOMER, 'CUSTOMER')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=254, unique=True, blank=False)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    pays = models.CharField(max_length=50, blank=True)
    role = models.CharField(choices=choice, default=CUSTOMER, max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    objects = UserManager()

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        ordering = ['created']

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.role}"
