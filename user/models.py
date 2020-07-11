from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager



class Exprience(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=)
    experince = models.CharField(max_length=500)