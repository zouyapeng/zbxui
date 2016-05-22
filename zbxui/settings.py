#coding:utf-8
"""
Django settings for zbxui project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q5hiv+9gnpw(k-+uelj$3jo_4_hutm8z4=6f0^t%z^9h*^fc%!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dashboard',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'zbxui.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'zbxui.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-CN'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

# ZABBIX_LIST = [{'idc':'周浦一期', 'address':'http://114.80.52.192:30119/', 'username':'zbxui', 'password':'zbxui', 'online':True},
#                {'idc':'斐讯一期', 'address':'http://218.245.64.3:10005/', 'username':'zbxui', 'password':'zbxui', 'online':True},
#                {'idc':'大连一期', 'address':'http://218.60.94.16/', 'username':'zbxui', 'password':'zbxui', 'online':True},
#                {'idc':'华通一期', 'address':'http://101.227.185.101:20021/', 'username':'zbxui', 'password':'zbxui', 'online':False},
#                {'idc':'公司测试', 'address':'http://58.247.8.188:10007/', 'username':'Admin', 'password':'zabbix', 'online':False}
# ]

ZABBIX_LIST = [{'idc':'周浦一期', 'address':'http://114.80.52.192:30119/', 'username':'zbxui', 'password':'zbxui', 'online':True},
               {'idc':'斐讯一期', 'address':'http://218.245.64.3:10005/', 'username':'zbxui', 'password':'zbxui', 'online':True},
               {'idc':'大连一期', 'address':'http://218.60.94.16/', 'username':'zbxui', 'password':'zbxui', 'online':True},
               {'idc':'华通一期', 'address':'http://101.227.185.101:20021/', 'username':'zbxui', 'password':'zbxui', 'online':False},
]