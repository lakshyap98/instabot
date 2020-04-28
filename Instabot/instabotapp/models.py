from django.db import models


class DetailAccount(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    caption = models.TextField()
    select_image = models.ImageField() 
    
