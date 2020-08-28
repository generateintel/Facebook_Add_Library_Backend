from django.contrib.auth.models import User
from django.shortcuts import render
import random
import re
import string
import requests
from django.contrib.auth.hashers import check_password
from django.core.mail import EmailMessage
from rest_framework.utils import json
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template.loader import get_template
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status, viewsets, mixins, generics, response

# Generate Jwt-Token
from rest_framework_jwt.settings import api_settings
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

#======================model ans serializer import
from Core.models import User_Profile

from .models import User_Profile
from .serializers import ProfileSerializer, ProfilePostSerializer, Contact_Us_Serializer
#================================Password Code
from password_strength import PasswordPolicy, stats
from password_strength import PasswordStats

policy = PasswordPolicy.from_names(
    length=8,  # min length: 8
    uppercase=1,  # need min. 2 uppercase letters
    numbers=2,  # need min. 2 digits
    special=2,  # need min. 2 special characters
    nonletters=2,  # need min. 2 non-letter characters (digits, specials, anything)
)

#=========================Function start
def emailsending(key,template,email,msg):
    message = get_template(template).render(key)
    email = EmailMessage(msg, message, to=[email])
    email.content_subtype = 'html'
    email.send()
    print('Email Snd Successfully')


def secret_key_generater():
    secret_id = ''.join(
        random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(200))
    return secret_id

def password_strenght(password):
    stats = PasswordStats(password)
    strenght = stats.strength()
    print(strenght)
    return strenght



#================================Views Start
class User_Profiles(viewsets.ViewSet):#User class
    @action(detail=False,methods=['post'])
    def Login(self, request):
        username=request.data["email"]
        password=request.data["password"]
        if User.objects.filter(username=username).exists():
            object_user=User.objects.get(username=username)
            user_profile_object=User_Profile.objects.get(user=object_user.id)
            if(user_profile_object.verfication_status==True):
                # newapi='http://52.116.74.57:9571/core/login/'
                newapi = 'http://127.0.0.1:8000/core/login/'
                data1 = {"username": object_user.username,
                         "password": password}
                response = requests.post(newapi, data=data1).json()
                if 'token' in response:
                    key = response['token']
                    return Response({"Token": key, "role": user_profile_object.role}, status=status.HTTP_200_OK)

                else:
                    return Response({"Message": "Wrong password"}, status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response({"Message":"Please Activate your Acccount"},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Message": "Wrong email"}, status=status.HTTP_404_NOT_FOUND)

    # {
    #     "email": "frazmirza58@gmail.com",
    #     "password": "FRAZdjbhh3545@/.."
    # }

    @action(detail=False, methods=['post'])
    def SignUp(self, request):  # user_Signup
        if User.objects.filter(Q(username=request.data['email'])).exists():
            # print(request.data['username'])
            return Response({"msg": "Already Registered"}, status.HTTP_306_RESERVED)
        else:
            if password_strenght(request.data['password']) > 0.25:
                print("New Record")
                if 'full_name' in request.data:
                    try:
                        fullsplit = str(request.data['full_name']).split(" ")
                        firstname = fullsplit[0]
                        lastname = fullsplit[1]
                        user = User.objects.create_user(first_name=firstname, last_name=lastname,
                                                        username=request.data['email'],
                                                        password=request.data['password'])
                    except:
                        firstname = request.data['full_name']
                        user = User.objects.create_user(first_name=firstname,
                                                        username=request.data['email'],
                                                        password=request.data['password'])

                if user != '':
                    email = request.data['email']
                    user = User.objects.get(username=email)
                    secret_id = secret_key_generater()
                    key = {
                        'link': 'http://localhost:63342/Active_Adds/Core/templates/Activation_Email.html/' + secret_id,
                        'username': firstname,
                        # 'link': 'http://192.168.30.225:7000/VerfiyEmail/' + secret_id
                    }
                    profile_obj = request.data
                    profile_obj.update({'user': user.id, 'activation_Key': secret_id})
                    del profile_obj['email']
                    del profile_obj['password']
                    serializer = ProfilePostSerializer(data=profile_obj)
                    if serializer.is_valid():
                        serializer.save()
                        print('doneeeeeeeeee')
                        emailsending(key, 'Activation_Email.html', email, 'Email Confirmation')
                        return Response({'Message': 'Successfully'}, status.HTTP_200_OK)
                    else:
                        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

                else:
                    return Response({'Message': 'Something went wrong'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"Message": "Weak password"}, status=status.HTTP_411_LENGTH_REQUIRED)

    @action(detail=False, methods=['post'])
    def Is_Activated(self, request):
        key = request.data['activation_Key']
        if User_Profile.objects.filter(activation_Key=key).exists():
            user = User_Profile.objects.get(activation_Key=key)
            if user.verfication_status == True:
                return Response({"msg": "Account already active"}, status=status.HTTP_403_FORBIDDEN)
            else:
                change_verication_status={"verfication_status":True}
                serializer = ProfilePostSerializer(user,data=change_verication_status,partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"msg": "Account Activated"}, status=status.HTTP_200_OK)

                else:
                    return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


        return Response({"msg": "Invalid Activation key"}, status=status.HTTP_400_BAD_REQUEST)

class Password(viewsets.ViewSet):#User class

    @action(detail=False, methods=['post'])
    def Forget_Password(self,request):#forget pass email
        email=request.data['email']
        print(email)
        if (User.objects.filter(username=email).exists()):
            user=User.objects.get(username=email)

            secret_id=secret_key_generater()
            pro=User_Profile.objects.get(user__id=user.id)
            pro.forget_password_key=secret_id
            pro.save()

            key = {
                'link': 'http://localhost:63342/Active_Adds/Core/templates//resetpassword/' + secret_id,
                'username': user.username,
            }
            emailsending(key, 'forgetpasssordbrand.html', email, 'Email Confirmation')
            return Response({"msg": "Okay"}, status.HTTP_200_OK)
        else:
            return Response({"msg": "Not valid Email"}, status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['post'])
    def Change_Password(self, request): #change password
        password= request.data['password']
        new_password= request.data['password']
        # new_password=request.data['new_password']
        code=request.data['activation_Key']
        # code=request.GET.get('code')
        # print("code",code)

        if password !='' and new_password !='':
            stats = PasswordStats(password)
            strenght=stats.strength()
            if strenght>0.25:
                if(password==new_password):
                    user=User_Profile.objects.get(forget_password_key=code)
                    main_user_id=user.user.id
                    change_password=User.objects.get(pk=main_user_id)
                    change_password.set_password(password)
                    change_password.save()
                    return Response({"msg":"Change Done"},status.HTTP_200_OK)

                else:
                    return  Response({"msg":"Not Match"},status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
            else:
                return Response({"msg": "Password min length: 8, need min. 2 digits, need min. 2 special characters ,eed min. 2 non-letter characters (digits, specials, anything)  "+ str(stats)}, status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        else:
            return Response({"msg":"fill all fileds"})

    # @permission_classes((IsAuthenticated,))
    # @action(detail=False, methods=['get', 'put'])
    # def User_Profile_Information(self, request):  # get user proifle data
    #     if request.method == 'GET':
    #         print(request.user)
    #         snippets = User_Profile.objects.get(user=request.user)
    #         serializer = ProfileSerializer(snippets)
    #         serializer = serializer.data
    #         data = serializer['user']
    #         # print(data)
    #         name = (serializer['profile_picture'])
    #         del serializer['user']
    #         serializer.update({'first_name': data['first_name'], 'last_name': data['last_name']})
    #         return Response(serializer)
    #
    #     elif request.method == 'PUT':
    #         user_id = User_Profile.objects.get(user=request.user.id)
    #         user = User.objects.get(id=request.user.id)
    #         keyword = request.data
    #         if 'first_name' in keyword:
    #             user.first_name = request.data['first_name']
    #         if 'last_name' in keyword:
    #             user.last_name = request.data['last_name']
    #
    #         if 'profile_picture' in keyword:
    #             print(request.data['profile_picture'])
    #             # user_id.profile_picture = request.data['profile_picture']
    #             #     with open(request.data['profile_picture'], 'rb') as f:
    #             #         contents = f.read()user
    #             #         print(contents)
    #             blob = bucket.blob('profile_picture/' + user.first_name + str(user.id) + '.png')
    #             blob.upload_from_filename(str(request.data['profile_picture']))
    #             # print(blob.acl)
    #             user_id.profile_picture = blob
    #             print(user_id.profile_picture)
    #         if 'gender' in keyword:
    #             user_id.gender = request.data['gender']
    #         if 'age' in keyword:
    #             user_id.age = request.data['age']
    #         if 'interest' in keyword:
    #             user_id.interest = request.data['interest']
    #         if 'mobile' in keyword:
    #             user_id.mobile = request.data['mobile']
    #         if 'location' in keyword:
    #             user_id.location = request.data['location']
    #         user_id.profile_updated = True
    #         user.save()
    #         user_id.save()
    #         #     serializer.save()
    #         return Response(user_id.profile_picture, status=status.HTTP_201_CREATED)


class ContactUs(viewsets.ViewSet):# class for contact us
    @action(detail=False, methods=['post'])
    def Post(self, request): #contact us post
        # user = request.data
        serializer = Contact_Us_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            key = {
                'username': request.data['name']
            }
            email=request.data['email']
            emailsending(key, 'contact_us.html', email, 'Email Confirmation')
            # emailsending(key, 'contact_us.html', request.data['Email'], 'Thanks for contacting with KingBestMall')
            return Response({'status': 'Thanks for contacting'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

