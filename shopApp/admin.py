from django.contrib import admin
from shopApp.models import*
from django.contrib.auth.models import Group

admin.site.site_header = 'Shop At Best'

admin.site.register(User_account)
admin.site.register(Client)
admin.site.register(Category)
admin.site.unregister(Group)

admin.site.register(BannerAddPage)
# admin.site.register(Person)
# # admin.site.register(MytypeField)


