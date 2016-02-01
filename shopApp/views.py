from django.shortcuts import render
from shopApp.models import*
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from django.db.models import Q
from shopApp.serializers import *
from rest_framework.generics import ListAPIView
import json
from datetime import date
from shopApp.models import*
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
from .pagination import ResultsSetPagination
# from django.utils import date
class Ad_view(ListAPIView):
    pagination_class = ResultsSetPagination
    serializer_class=BannerAddPage_Serializer
    def get_queryset(self):
        queryset = BannerAddPage.objects.filter (Q(ad_status='Live') & Q(ad_liveDateFrom__lte= date.today() )& Q(ad_liveFromTo__gte = date.today())).order_by('-banner_position')
        return queryset
class Ad_search_view(ListAPIView):
    pagination_class = ResultsSetPagination
    serializer_class=BannerAddPage_Serializer
    def get_queryset(self):
        key=str(self.request.GET.get('key'))
        queryset=BannerAddPage.objects.filter(Q(key__icontains=key) & Q(ad_status='Live') & Q(ad_liveDateFrom__lte= date.today() )& Q(ad_liveFromTo__gte = date.today())).order_by('-banner_position')
        return queryset






