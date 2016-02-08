from django.contrib import admin
from shopApp.models import*
from django.contrib.auth.models import Group


admin.site.register(BannerAddPage)
admin.site.register(User_account)
admin.site.register(Client)
admin.site.register(Category)
admin.site.unregister(Group)
# admin.site.register(Track_user)
# admin.site.register(First_download)


