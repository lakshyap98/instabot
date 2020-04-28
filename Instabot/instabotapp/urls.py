from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.FormPosting.as_view(), name='formpost'),
    path('success/', views.successf, name='successurl'),
    path('error/', views.errorf, name='errorurl'),
]
