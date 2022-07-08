from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

class Login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)