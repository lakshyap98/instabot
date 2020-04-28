from django.db import models
from django.urls import reverse
# Create your models here.

class Product(models.Model):
    title       = models.CharField(max_length=100)
    desc        = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=10000)
    summary     = models.TextField(blank = True, null = True)
    featured    = models.BooleanField()
    slug = models.SlugField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return f"../detail/{self.id}/"
        return reverse("detail", kwargs={"id": self.id})