from django.shortcuts import render
from shopApp.models import*
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from shopApp.serializers import *
from rest_framework.generics import ListAPIView
import json
from shopApp.models import*
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
from .pagination import ResultsSetPagination

class Ad_view(ListAPIView):
    pagination_class = ResultsSetPagination
    serializer_class=BannerAddPage_Serializer
    def get_queryset(self):
        queryset = BannerAddPage.objects.all().order_by('-banner_position')
        return queryset
def login_view(self,request):
	return HttpResponse("ok")




