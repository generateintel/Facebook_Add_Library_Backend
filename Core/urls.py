# import Views as Views
from django.conf.urls import url, include
from django.urls import path,include
# from django.urls import
# from .views import *
from . import views
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token,verify_jwt_token
from .views import *

# urlpatterns = [

# ]

router=routers.DefaultRouter()
router.register(r'User', User_Profiles, 'User')#User apis
router.register(r'User', Password, 'User')#User apis to change password


urlpatterns=[
    path('', include(router.urls)),
    path('login/', obtain_jwt_token),#login
    # path("sociallogin/", sociallogin.as_view({'post': 'create'})),  # View User Profile Details

]