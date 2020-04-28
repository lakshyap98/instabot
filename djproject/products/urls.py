"""myapplication URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('<int:id>/', views.home_view),
    path('', views.product_create_view),
    # path('', views.rawproduct_create_view),
    path('initial/', views.render_initial_data),
    path('detail/<int:id>/', views.product_detail, name="detail"),
    path('detail/<int:id>/delete', views.product_delete, name="delete"),
    path('list/', views.product_list, name="list"),
]
