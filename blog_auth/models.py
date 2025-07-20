from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False)
    is_blocked = models.BooleanField(default=False)

    def __str__(self):
        return self.username