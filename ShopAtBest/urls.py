from django.conf.urls import patterns, include, url
from django.contrib import admin
from shopApp import views
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns
from shopApp.forms import MyAuthenticationForm

admin.autodiscover()
admin.site.login_form = MyAuthenticationForm
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ShopAtBest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^admin/login/', views.login_view),
    url(r'^add/',include('shopApp.urls')),
    url(r'^search/',include('shopApp.urls')),
    )

urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))