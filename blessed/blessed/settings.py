"""
Django settings for blessed project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
#try 4 of gitignore
from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-i)9+nd(m1ermdrg2091pjyju@46u4v1#yegv6(_905j9d8$ve)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "crispy_forms",
    'main.apps.MainConfig',
    'register.apps.RegisterConfig',
    'django_mysql',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blessed.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'blessed.wsgi.application'
STRIPE_SECRET_KEY="sk_test_51M6dQHLUoQwS73Adxh3Dat5mqvFBTo2V33xOyuHTvWR3MIEqBGNB8DSIn5OzOfIRdJoMpW3ytN3ai6Qhnsx89EH000z61ztooP" 
STRIPE_PUBLIC_KEY="pk_test_51M6dQHLUoQwS73AdpvDRcFzQEhEjrZNLv6nEKvMINOuQeQBodB1w8IqyDPNcbVlm4IwkdA0dh7BPtGs2t0tA1Mi300R9aNf7kJ"

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.sqlite3',  
        'NAME': BASE_DIR / 'db.sqlite3',  
    }
}    
# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = '/'




#mail sending 
# drsooetfjhjnhfns 
 
EMAIL_HOST = 'smtp.gmail.com' 
EMAIL_USE_TLS = True 
EMAIL_PORT = 587 
EMAIL_HOST_USER = 'blessedstore.sk@gmail.com' 
EMAIL_HOST_PASSWORD = 'drsooetfjhjnhfns' 
# Static files (CSS, JavaScript, Images) 
# https://docs.djangoproject.com/en/4.0/howto/static-files/ 
 
LOGIN_REDIRECT_URL = "/" 
LOGOUT_REDIRECT_URL = "/" 
 
 
 
 
 

STATIC_URL = 'static/static/static/static/static/'
STATICFILES_DIRS = (
   os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = 'static/static/static/static/images/' 
if DEBUG: 
    MEDIA_URL = 'static/images/' 
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images') 

CRISPY_TEMPLATE_PACK="bootstrap4"
 
# Default primary key field type 
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field 
 
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'