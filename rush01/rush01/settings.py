"""
Django settings for rush01 project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*8ktj0=o_^%=_xnql7n2bel2=!=#!lry6j@cemmnyytr4ui6z$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [

	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'bootstrap3',
	# deployed apps
	'app_example',
	'myauth',
	'forum',
	'userprofile',
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

ROOT_URLCONF = 'rush01.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [
			os.path.join(BASE_DIR, 'templates/')
		],
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

WSGI_APPLICATION = 'rush01.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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


LOGIN_URL = 'myauth-login'
#LOGIN_REDIRECT_URL = '/'


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Bootstrap

BOOTSTRAP3 = {
	# The URL to the jQuery JavaScript file
	'jquery_url': '//code.jquery.com/jquery.min.js',

	# The Bootstrap base URL
	'base_url': '//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/',

	# The complete URL to the Bootstrap CSS file (None means derive it from base_url)
	'css_url': None,

	# The complete URL to the Bootstrap CSS file (None means no theme)
	'theme_url': None,

	# The complete URL to the Bootstrap JavaScript file (None means derive it from base_url)
	'javascript_url': None,

	# Put JavaScript in the HEAD section of the HTML document (only relevant if you use bootstrap3.html)
	'javascript_in_head': False,

	# Include jQuery with Bootstrap JavaScript (affects django-bootstrap3 template tags)
	'include_jquery': False,

	# Label class to use in horizontal forms
	'horizontal_label_class': 'col-md-3',

	# Field class to use in horizontal forms
	'horizontal_field_class': 'col-md-9',

	# Set HTML required attribute on required fields
	'set_required': True,

	# Set HTML disabled attribute on disabled fields
	'set_disabled': False,

	# Set placeholder attributes to label if no placeholder is provided
	'set_placeholder': True,

	# Class to indicate required (better to set this in your Django form)
	'required_css_class': '',

	# Class to indicate error (better to set this in your Django form)
	'error_css_class': 'has-error',

	# Class to indicate success, meaning the field has valid input (better to set this in your Django form)
	'success_css_class': 'has-success',

	# Renderers (only set these if you have studied the source and understand the inner workings)
	'formset_renderers':{
		'default': 'bootstrap3.renderers.FormsetRenderer',
	},
	'form_renderers': {
		'default': 'bootstrap3.renderers.FormRenderer',
	},
	'field_renderers': {
		'default': 'bootstrap3.renderers.FieldRenderer',
		'inline': 'bootstrap3.renderers.InlineFieldRenderer',
	},
}



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# media files

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')