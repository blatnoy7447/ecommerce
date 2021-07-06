from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    user_type_choices=((1,"Admin"), (2,"Staff"), (3,"Merchant"), (4, "Customer"))
    user_type=models.CharField(max_length=255, choices=user_type_choices, default=1)


class AdminUser(models.Model):
    profile_pic = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)


class StaffUser(models.Model):
    profile_pic = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)


class Merchant(models.Model):
    profile_pic = models.ImageField()
    company_name = models.CharField(max_length=255)
    gst_details = models.CharField(max_length=255)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class CustomerUser(models.Model):
    profile_pic = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)


class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    url_slug = models.CharField(max_length=255)
    thumbnail = models.FileField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
