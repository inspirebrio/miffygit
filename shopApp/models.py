from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import *
from django.contrib.auth import *
from django.db import models
from datetime import datetime
import base64
from datetime import date
from django.core.validators import ValidationError
from django.contrib.admin.widgets import AdminDateWidget 
from django.contrib.admin import widgets
# from shopApp import settings


class AccountManager(BaseUserManager):
	"""This model is used for signup purpose."""
	def create_user(self, email, password=None, **kwargs):
		"""This method is used for crate user (client) for accessing resources."""
		if not email:
			raise ValueError('Users must have a valid email address.')

		if not kwargs.get('username'):
			raise ValueError('Users must have a valid username.')

		account = self.model(
			email=self.normalize_email(email), username=kwargs.get('username')
		)

		account.set_password(password)
		account.save()

		return account

	def create_superuser(self, email, password, **kwargs):
		"""This method is used for create super user(like admin)."""
		account = self.create_user(email, password, **kwargs)

		account.is_admin = True
		account.is_staff= True
		account.is_superuser=True	
		account.is_active=True
		account.save()

		return account

class User_account(AbstractBaseUser,PermissionsMixin):
	BOOL_CHOICES = ((True, 'Live'), (False, 'Pause'))

	name=models.CharField(max_length=200,blank=True,null=True)
	email=models.EmailField(unique=True,blank=True,null=True)
	username=models.CharField(unique=True,max_length=200,blank=True,null=True)
	#password=models.CharField(max_length=500)
	is_active=models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
	is_staff = models.BooleanField(('staff status'), default=False,help_text="<font color='green'>*Designates whether the user can log into this admin site(important).</font>")
	is_client=models.BooleanField(default=False)
	# created_at = models.DateTimeField(auto_now_add=True)
	# updated_at = models.DateTimeField(auto_now=True)
	mobile=models.CharField(max_length=15,blank=True,null=True)

	objects = AccountManager()
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']
	def __unicode__(self):
		return unicode(self.email)

	def get_full_name(self):
		return self.name
	def get_short_name(self):
		return self.name
	def __unicode__(self):
		"""It is overrided method and used for return **slug** **Symptoms_with_condition**"""
		return str(self.email)
	def save(self, *args, **kwargs):
		# self.set_password(self.password)
		super(User_account, self).save(*args, **kwargs)

class Client(models.Model):
	user_account=models.OneToOneField(User_account,unique=True,related_name='Client')
	address=models.CharField(max_length=950,null=True,blank=True)

	def __unicode__(self):
		"""It is overrided method and used for return **slug** **Symptoms_with_condition**"""
		return str(self.user_account)
class Category(models.Model):
	category_name=models.CharField(max_length=200,null=True,blank=True)
	category_description=models.CharField(max_length=800,null=True,blank=True)

	def __unicode__(self):
		"""It is overrided method and used for return **slug** **Symptoms_with_condition**"""
		return str(self.category_name)

def upload_to1(instance, filename):
	# print "name:",instance.client.user_account.name
	# print "URL :",'client/%s/%s/%s%s' % (instance.client.user_account.name,instance.ad_name,instance.ad_name,datetime.now()
	return base64.b64encode('client/%s/%s/%s%s' % (instance.client.user_account.name,instance.ad_name,instance.ad_name,datetime.now()))
# def upload_to2(instance, filename):-
# 	return 'client/,%s,%s' % (instance.id,datetime.now())
# def upload_to3(instance, filename):
# 	return 'client/,%s,%s' % (instance.id,datetime.now())
	# return 'user,' % (instance.id,datetime.now())

# class Banner(models.Model):
# 	ad_banner=models.ImageField(upload_to=upload_to,blank=True,null=True)
# 	ad_url=models.URLField(max_length=200,blank=True,null=True)
# from django.core.exceptions import ValidationError

# def is_valid_field(self, field_data, all_data):
#     if hasattr(models, field_data) and issubclass(getattr(models, field_data), models.Field):
#         # It exists and is a proper field type
#         print all_data
#         return
    
#     raise ValidationError("This is not a valid field type.") 

class BannerAddPage(models.Model):

   	BOOL_CHOICES = ((True, 'Live'), (False, 'Pause'))
   	TYPE_CHOICES = (('text', 'text'), ('image', 'image'))
   	ad_type=models.CharField(choices=TYPE_CHOICES,default=True,max_length=800)
	category=models.ForeignKey(Category,blank=True)
	client=models.ForeignKey(Client)
	# client_name=models.CharField(max_length=200,null=True)
	ad_type=models.CharField(choices=TYPE_CHOICES,default=True,max_length=800)
	ad_name=models.CharField(max_length=800,null=True,blank=True)
	ad_title=models.CharField(max_length=800,null=True,blank=True)
	ad_description=models.CharField(max_length=500)
	ad_status=models.BooleanField(choices=BOOL_CHOICES,default=True)
	ad_banner1=models.ImageField(upload_to=upload_to1,blank=True,null=True,help_text="<font color='green'>*You should upload a image file between 60px height and 60px width resolution</font>")
	ad_url1=models.URLField(max_length=800,blank=True,null=True)
	ad_banner2=models.ImageField(upload_to=upload_to1,blank=True,null=True,help_text="<font color='green'>*You should upload a image file between 60px height and 60px width resolution</font>")
	ad_url2=models.URLField(max_length=800,blank=True,null=True)
	ad_banner3=models.ImageField(upload_to=upload_to1,blank=True,null=True,help_text="<font color='green'>*You should upload a image file between 60px height and 60px width resolution</font>")
	ad_url3=models.URLField(max_length=800,blank=True,null=True)
	ad_liveDateFrom=models.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.",null=True)
	ad_liveFromTo=models.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.",null=True)
	key=models.CharField(max_length=800,blank=True,null=True)
	banner_position=models.IntegerField(default=0)

	def __unicode__(self):
		"""It is overrided method and used for return **slug** **Symptoms_with_condition**"""
		return str(self.ad_name)

# class Track_user(models.Model):

# 	ip_address = models.CharField(max_length=50,null=True,blank=True)
# 	browser = models.CharField(max_length=50,null=True,blank=True)
# 	date = models.DateField(auto_now_add=True)
# # 	
# 	def __unicode__(self):
# 		"""It is overrided method and used for return **slug** **Symptoms_with_condition**"""
# 		return str(self.ip_address)


# class First_download(models.Model):
	
# 	ip_address = models.CharField(max_length=50,null=True,blank=True)
# 	browser = models.CharField(max_length=50,null=True,blank=True)
# 	date = models.DateField(auto_now_add=True)
# 	def __unicode__(self):
# 		"""It is overrided method and used for return **slug** **Symptoms_with_condition**"""
# 		return str(self.ip_address)



