from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.text import gettext_lazy as _
from .managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    phoneno = PhoneNumberField(max_length=20,unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['email', 'name', 'phoneno']


'''#phone = models.TextField(max_length=20, blank=False)
    #is_verified = models.BooleanField(default=False)'''