"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 3.0.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qyu(9l9v%^+r(vt#ecf+36#lis516#3bo5@bo-rd*d%a=!%8#!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# from firebase_admin import initialize_app
import firebase_admin
from firebase_admin import credentials
#ALLOWED_HOSTS = ['.vercel.app', '.now.sh']
#ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["*", '127.0.0.1'])
# added vercel.app and now.sh to allowed hosts

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "pushy",

    "fcm_django",

    'widget_tweaks',                            # uses 'django-widget-tweaks' app
    'crispy_forms',                             # uses 'django-crispy-forms' app
    'login_required',                           # uses 'django-login-required-middleware' app

    'homepage.apps.HomepageConfig',
    'inventory.apps.InventoryConfig',
    'transactions.apps.TransactionsConfig',

]

# PUSHY_API_KEY = "AAAAD2tLd64:APA91bF268JRv-5AvmTs3_Dzejj326HcmiTpxX4wCBZODe49c8tU3vwcKL_KWLBSfBnFjwXksJHG6QmTa-oiyeZucHHd3lQEai6FMId4M6U8R0A7-SO66YiUbEip2Nayk24KRvT_ih73"
# PUSHY_SENDER_ID = "66224617390"

FCM_DJANGO_SETTINGS = {
    "FCM_SERVER_KEY": "AAAAD2tLd64:APA91bF268JRv-5AvmTs3_Dzejj326HcmiTpxX4wCBZODe49c8tU3vwcKL_KWLBSfBnFjwXksJHG6QmTa-oiyeZucHHd3lQEai6FMId4M6U8R0A7-SO66YiUbEip2Nayk24KRvT_ih73"
}

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_CREDENTIALS = True

## FIREBASE 
# FIREBASE_APP = initialize_app()

# FCM_DJANGO_SETTINGS = {
#      # an instance of firebase_admin.App to be used as default for all fcm-django requests
#      # default: None (the default Firebase app)
#     "DEFAULT_FIREBASE_APP": None,
#      # default: _('FCM Django')
#     "APP_VERBOSE_NAME": "[string for AppConfig's verbose_name]",
#      # true if you want to have only one active device per registered user at a time
#      # default: False
#     "ONE_DEVICE_PER_USER": False,
#      # devices to which notifications cannot be sent,
#      # are deleted upon receiving error response from FCM
#      # default: False
#     "DELETE_INACTIVE_DEVICES": True,
#     # Transform create of an existing Device (based on registration id) into
#                 # an update. See the section
#     # "Update of device with duplicate registration ID" for more details.
#     # default: False
#     "UPDATE_ON_DUPLICATE_REG_ID": True,
# }


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'login_required.middleware.LoginRequiredMiddleware',    # middleware used for global login
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],  # included 'templates' directory for django to access the html templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = os.path.join(BASE_DIR, 'static'),
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')


CRISPY_TEMPLATE_PACK = 'bootstrap4'                     # bootstrap template crispy-form uses

LOGIN_REDIRECT_URL = 'home'                             # sets the login redirect to the 'home' page after login

LOGIN_URL = 'login'                                     # sets the 'login' page as default when user tries to illegally access profile or other hidden pages

LOGIN_REQUIRED_IGNORE_VIEW_NAMES = [                    # urls ignored by the login_required. Can be accessed with out logging in
    'login',
    'logout',
    'about',
]

PROJECT_APP = os.path.basename(BASE_DIR)
cred = credentials.Certificate(os.path.join(PROJECT_APP, '/home/sherif/InvFlow/core/cred.json'))
firebase_admin.initialize_app(cred)
# print(cred)