from django.conf.urls import patterns, include, url
from django.contrib import admin
from shopApp import views

urlpatterns = patterns('',
	
    url(r'^page/',views.Ad_view.as_view()),
    url(r'^ad/$',views.Ad_search_view.as_view()),
)
