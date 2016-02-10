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
from ipware.ip import get_ip
from user_agents import parse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

# from django.utils import date
class Ad_view(ListAPIView):
    pagination_class = ResultsSetPagination
    serializer_class=BannerAddPage_Serializer
    def get_queryset(self):
        queryset = BannerAddPage.objects.filter(Q(ad_status='Live') & Q(ad_liveDateFrom__lte= date.today() )& Q(ad_liveFromTo__gte = date.today())).order_by('-banner_position')
        return queryset
class Ad_search_view(ListAPIView):
    pagination_class = ResultsSetPagination
    serializer_class=BannerAddPage_Serializer
    def get_queryset(self):
        key=str(self.request.GET.get('key'))
        print 'u here',key
        queryset=BannerAddPage.objects.filter(Q(key__icontains=key) & Q(ad_status='Live') & Q(ad_liveDateFrom__lte= date.today() )& Q(ad_liveFromTo__gte = date.today())).order_by('-banner_position')
        return queryset


# class Track_user1(APIView):
#     def get(self,request):
#         ip = get_ip(request)
#         browser = request.META['HTTP_USER_AGENT']
#         user_agent = parse(browser)
#         print "IP ",ip
#         print "BROWSER",user_agent.browser.family
#         track = Track_user.objects.create(ip_address=ip,browser=user_agent.browser.family)
#         track.save()


#         return redirect('http://www.google.com')

# class First_download1(APIView):
#     def get(self,request):
#         ip = get_ip(request)
#         browser = request.META['HTTP_USER_AGENT']
#         user_agent = parse(browser)
#         print "IP ",ip
#         print "BROWSER",user_agent.browser.family
#         first = First_download.objects.create(ip_address=ip,browser=user_agent.browser.family)
#         first.save()
#         return HttpResponse('Ok')

# class Ip_matching(APIView):
#     def get(self,request):
#         data=Track_user.objects.all()
#         data1=First_download


