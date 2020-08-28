from django.contrib.auth.models import User
from rest_framework import serializers

from .models import User_Profile, Contact_Us


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class ProfileSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    class Meta:
        model=User_Profile
        fields=['user','profile_picture', 'gender','age','interest','mobile','location']

# class AdminUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=User
#         fields='__all__'
# class AdminSerializer(serializers.ModelSerializer):
#     user=AdminUserSerializer()
#     class Meta:
#         model=User_Profile
#         fields='__all__'
#
#
class ProfilePostSerializer(serializers.ModelSerializer):
    class Meta:
        model=User_Profile
        fields=['user','profile_picture', 'gender','age','interest','mobile','location','verfication_status','activation_Key']
#
class Contact_Us_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Contact_Us
        fields=['name','email','phone','message','created_date','modified_date']
#
#
# # class Instructor_Serializer(serializers.Serializer):
# #     # category=CategorySerializer()
# #     class Meta:
# #         model=Instructor
# #         fields=['id','name','title','profile_picture','description','is_active','category','created_date','modified_date']
#
#
# class Instructor_Serializer_save(serializers.ModelSerializer):
#     # category=CategorySerializer()
#     class Meta:
#         model=Instructor
#         fields=['id','name','title','profile_picture','description','is_active','category','created_date','modified_date']
#
# class Instructor_Serializer(serializers.ModelSerializer):
#     category = CategorySerializer()
#     class Meta:
#         model=Instructor
#         fields=['id','name','title','profile_picture','description','is_active','category','created_date','modified_date']
#
# class Instructor_Serializer_Homepage(serializers.ModelSerializer):
#     class Meta:
#         model=Instructor
#         fields=['name','title','profile_picture']
#
# # class Instructor_Announcements_Serializer(serializers.ModelSerializer):
# #     instructor_announcements=Instructor_Serializer(source='instructor',read_only=True)
# #     class Meta:
# #         model=Instructor_Announcements
# #         fields=['id','description','screenshot','instructor_announcements','social_media_name','is_active','created_date','modified_date']
#
# # ,'instructor'
# class Instructor_Announcements_Serializer(serializers.ModelSerializer):
#     instructor_announcements=Instructor_Serializer(source='instructor', read_only=True)
#     class Meta:
#         model=Instructor_Announcements
#         fields=['id','instructor','description','screenshot','social_media_name','social_media_username','is_active','created_date','modified_date','instructor_announcements']
