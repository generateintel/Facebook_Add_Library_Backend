from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Advertisers,Category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'
class AdvertiserSerializer(serializers.ModelSerializer):
    category=CategorySerializer()
    class Meta:
        model=Advertisers
        # fields='__all__'
        fields=['id','category','image_url', 'page_name','page_likes','followers','page_created_date','company_type','people_manage_page','countries_manage_page','active_add','inactive_add']

