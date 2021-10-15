""""Post models"""

# Djagno
from django.db import models
from django.db.models.fields import DateField

class User(models.Model):
    """User model."""
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    is_admin = models.BooleanField(default=False)

    # Tiene mas caracteres que un CharField
    bio = models.TextField(blank=True)

    birthdate = models.DateField(blank=True, null=True)

    country = models.CharField(max_length=50, null=True)

    # Este alamcena también la hora
    created = models.DateTimeField(auto_now_add=True) # Guarda la fecha de creación
    modified = models.DateTimeField(auto_now=True) # Guarda la fecha de ultima edición

    def __str__(self):
        """Return self.email"""
        return self.email
