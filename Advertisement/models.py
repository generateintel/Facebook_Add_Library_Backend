from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=255, blank=True)
    icon=models.TextField(blank=True,null=True)
    hide=models.BooleanField(default=False,null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


class Advertisers(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    fb_page_link = models.CharField(max_length=1000, blank=True)
    fb_page_id = models.CharField(max_length=1000, blank=True,null=True)
    image_url = models.CharField(max_length=1000, null=True, blank=True)
    page_name=models.CharField(max_length=255, blank=True,null=True)
    page_likes=models.BigIntegerField(default=0,null=True)
    followers=models.BigIntegerField(default=0,null=True)
    page_created_date=models.DateField(blank=True,null=True)#Date Formate must be this year-month-day
    company_type=models.CharField(max_length=255, blank=True,null=True)
    people_manage_page=models.BigIntegerField(default=0,null=True)
    countries_manage_page=models.BigIntegerField(default=0,null=True)
    active_add=models.BigIntegerField(default=0,null=True)
    inactive_add=models.BigIntegerField(default=0,null=True)
    is_active=models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


