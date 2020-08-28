import json
import types

from django.db.models import Q
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from rest_framework import viewsets, generics, mixins, status
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from Advertisement.custom_pagination import Pagination,Filter_Pagination
from .serializers import AdvertiserSerializer
from .models import Advertisers, Category

# Create your views here.





class Top_Advertisers(viewsets.ViewSet):#Show all Add data
    @action(detail=False, methods=['get'])
    def Facebook_Page_Add(self, request):
        p1 = Pagination(request,Advertisers,'modified_date',2,AdvertiserSerializer)
        res=p1.split_instances_into_pagination()
        return Response(res)

    @action(detail=False, methods=['get'])
    def test(self, request):
        return Response("okay")
# Advertisers.objects.filter(page_likes__lte=3556)

class Filters(viewsets.ViewSet):#Applt filters in data.
    @action(detail=False, methods=['get'])
    def Facebook_Page_Add_filters(self, request):
        q=Q()
        filter_list=['category','is_active','page_likes__gte','page_likes__lte','followers__gte','followers__lte','active_add__gte','active_add__lte','inactive_add__gte','inactive_add__lte']
        your_filters = {}
        for index ,item in enumerate(filter_list, start=1):
            if index==1:
                if item in request.GET:
                    try:

                        category_url = request.GET[item]
                        # print(category_url)
                        category_instance=Category.objects.get(category_name__exact=category_url)
                        # fraz=filter_list[index]
                        q &=Q(item=category_instance)
                        print(q)
                        # your_filters.update({item:category_instance})
                        # print(your_filters)
                    except:
                        return Response("Wrong Category",status=status.HTTP_400_BAD_REQUEST)

                else:
                    return Response("Need Category in url ",status=status.HTTP_400_BAD_REQUEST)
            else:
                if item in request.GET:

                    q &=Q(item=request.GET[item])
                    # print(q)
                    # print(request.GET[item])
                    # your_filters.update({item:request.GET[item]})
                    # print(your_filters)
                else:pass
        if request.method == "GET":

            filter_data = Advertisers.objects.complex_filter(q)
            if len(filter_data)>0:
                # serializer = AdvertiserSerializer(filter_data, many=True)
                # return Response(serializer.data,status=status.HTTP_200_OK)
                p1 = Filter_Pagination(request, filter_data, 'modified_date', 1, AdvertiserSerializer)
                res = p1.split_instances_into_pagination()
                return Response(res,status=status.HTTP_200_OK)
            else:
                return Response("Not Found",status=status.HTTP_404_NOT_FOUND)



