from django.contrib.auth.models import AbstractUser
from django.db import models
from blog.models import Category

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False)
    is_blocked = models.BooleanField(default=False)
    # Add the ManyToMany field for subscribed categories
    subscribed_categories = models.ManyToManyField(
        Category,
        related_name='subscribers',
        blank=True
    )
    
    def __str__(self):
        return self.username