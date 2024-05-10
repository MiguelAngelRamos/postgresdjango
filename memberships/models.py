from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    
    health_details = models.TextField(blank=True, null=True)
    preferred_activities = models.CharField(max_length=100, blank=True, null=True)
    
    # Iniciar session con el campo de email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    