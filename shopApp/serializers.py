from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *

class BannerAddPage_Serializer(serializers.ModelSerializer):
   # body_part = Body_partSerializer(many=True)
    # image_url = serializers.SerializerMethodField()
    ad_url1 = serializers.SerializerMethodField()
    ad_url2 = serializers.SerializerMethodField()
    ad_url3 = serializers.SerializerMethodField()

    class Meta:
        model = BannerAddPage
        fields = ('ad_name','ad_title','ad_description','ad_banner1','ad_url1','ad_banner2','ad_url2','ad_banner3','ad_url3','ad_type','banner_position')

    # def get_image_url(self,obj):
    	
    #     return 'http:/'+obj.ad_banner1.path
    def get_ad_url1(self,obj):
        return obj.ad_url1

    def get_ad_url2(self,obj):
        return obj.ad_url2
        
    def get_ad_url3(self,obj):
        return obj.ad_url3

