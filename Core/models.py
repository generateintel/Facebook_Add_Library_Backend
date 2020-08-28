from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class User_Profile(models.Model):
    ROLE_CHOICES = (
        ('A', 'Admin'),
        ('S', 'Super'),
        ('U', 'User'),
        ('V', 'Vendor'),
    )
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='0')
    profile_picture = models.TextField(blank=True,)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,blank=True)
    age=models.CharField(max_length=255,blank=True)
    interest=models.CharField(max_length=255,blank=True)
    mobile = models.CharField(max_length=255,blank=True)
    location = models.CharField(max_length=255,blank=True)
    role = models.CharField(max_length=1, choices=ROLE_CHOICES, default='U')
    verfication_status = models.BooleanField(default=False)
    activation_Key = models.CharField(max_length=255, blank=True, default='')
    user_deactive_status=models.CharField(max_length=255, blank=True, default='')
    user_deactive_reason=models.CharField(max_length=255, blank=True, default='')
    forget_password_key=models.TextField(blank=True)
    profile_updated=models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.user)

class Contact_Us(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    message = models.CharField(max_length=10000000, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)