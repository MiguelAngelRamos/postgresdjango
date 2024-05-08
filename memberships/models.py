from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    health_details = models.TextField(blank=True, null=True)
    preferred_activities = models.CharField(max_length=100, blank=True, null=True)
