from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields.json import DataContains

class Profile(models.Model):
    """Profile model.
    
    Proxy model that extendes the base data with other 
    information
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(max_length=200, blank=True)
    biografy = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    
    picture = models.ImageField(
        upload_to='users/pictures', 
        blank=True, 
        null=True
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return username"""
        return self.user.username
