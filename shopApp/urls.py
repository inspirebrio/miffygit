from django.conf.urls import patterns, include, url
from django.contrib import admin
from shopApp import views

from django.views.generic import RedirectView
# from django.views.generic.simple import redirect_to

urlpatterns = patterns('',

    url(r'^page/',views.Ad_view.as_view()),
    url(r'^ad/$',views.Ad_search_view.as_view()),
    # url(r'^track/$',views.Track_user1.as_view()),
    # url(r'^first/$',views.First_download1.as_view()),
    # url(r'^redirect/$',RedirectView.as_view(url='www.google.com')),

)