from django.db import models
from django.urls import reverse

class UserDetails(models.Model):
    username = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=100)
    user_pp = models.FileField(upload_to='profile_pictures/', null=False, blank=False)
    phone_number = models.IntegerField(unique=True)

    def __str__(self):
        return self.username
    
    def get_absolute_url(self):
        return reverse('blogapp:login')