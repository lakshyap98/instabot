from django.contrib import admin
from .models import Article
# Register your models here.

class Articleactions(admin.ModelAdmin):
    list_display = ("title", "active")
    # fields = '__all__'
    
admin.site.register(Article, Articleactions)