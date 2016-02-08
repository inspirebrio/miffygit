from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *

class BannerAddPage_Serializer(serializers.ModelSerializer):
   # body_part = Body_partSerializer(many=True)
    # image_url = serializers.SerializerMethodField()
    add_url = serializers.SerializerMethodField()

    class Meta:
        model = BannerAddPage
        fields = ('ad_name','ad_title','ad_description','ad_banner1','ad_banner2','ad_banner3','add_url','ad_type','banner_position')

    # def get_image_url(self,obj):
    	
    #     return 'http:/'+obj.ad_banner1.path
    def get_add_url(self,obj):
    	
        return obj.ad_url1

