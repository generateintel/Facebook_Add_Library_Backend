# import Views as Views
from django.conf.urls import url, include
from django.urls import path,include
from rest_framework import routers
from .views import *

# urlpatterns = [

# ]

router=routers.DefaultRouter()
router.register(r'Advertiser', Top_Advertisers, 'Advertisers')#Top Add
router.register(r'Filters(?:/(?P<id>[0-9]+))?', Filters, 'Filters')#Filters Add


urlpatterns=[
    path('', include(router.urls)),

]