from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    """
    Custom user model that extends the default Django User model.
    This can be used to add additional fields or methods in the future.
    """
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='pfp/', blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.username