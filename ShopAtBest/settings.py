"""
Django settings for ShopAtBest project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7nslvrl-2)%1ed6ok9d30%0x(91o-4110ycb%4nnk5r$=zqm43'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
STATIC_PATH = os.path.join(BASE_DIR, 'static')
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']



# Application definition

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'shopApp',
    'debug_toolbar',
    'corsheaders',
    'storages'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ShopAtBest.urls'
CORS_ORIGIN_ALLOW_ALL = True
WSGI_APPLICATION = 'ShopAtBest.wsgi.application'

CROS_ORIGIN_ALLOW_ALL=True

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'miffydb',
        'USER' : 'miffyuser',
        'PASSWORD' : 'miffy24x7',
        'HOST' :'miffypsql.ch79fqaqul7s.ap-southeast-1.rds.amazonaws.com',
        'PORT' : '5432',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AWS_STORAGE_BUCKET_NAME = 'mifymediabucket'
AWS_ACCESS_KEY_ID = 'AKIAI3Q6B44BEF3RFYZA'
AWS_SECRET_ACCESS_KEY = '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'

    # Tell django-storages that when coming up with the URL for an item in S3 storage, keep
    # it simple - just use this domain plus the path. (If this isn't set, things get complicated).
    # This controls how the `static` template tag from `staticfiles` gets expanded, if you're using it.
    # We also use it in the next setting.
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

    # This is used by the `static` template tag from `static`, if you're using that. Or if anything else
    # refers directly to STATIC_URL. So it's safest to always set it.
STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN

    # Tell the staticfiles app to use S3Boto storage when writing the collected static files (when
    # you run `collectstatic`).
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
#MEDIA_URL='/media/'
#STATIC_ROOT=STATIC_PATH
#STATIC_URL = '/static/'


AUTH_USER_MODEL = 'shopApp.User_account'
