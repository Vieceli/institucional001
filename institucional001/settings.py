# Django settings for institucional001 project.
import os
PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
FORCE_SCRIPT_NAME = ''
DEFAULT_CITY_SLUG = '/site/goiania/'
LOGIN_URL = "/usuario/login/"
LOGIN_REDIRECT_URL = "/"

#informacoes sistema
AUTH_PROFILE_MODULE = 'accounts.userprofile'
SITE_NAME = 'Clipper Magazine Brasil'
META_KEYWORDS = 'Descontos, Cupons, Gratuito,Compra,Coletiva'
META_DESCRIPTION = 'Site de compras coletivas'
SESSION_COOKIE_AGE = 7776000 # the number of seconds in 90 days

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'veiodruida@gmail.com'
EMAIL_HOST_PASSWORD = 'cogumelos1206'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


ADMINS = (
  ('Jhoni', 'veiodruida@gmail.com'),
  ('Miltinho Brandao', 'miltinho@gmail.com'),
  ('Marinho Brandao', 'marinho@gmail.com'),
)
MANAGERS = ADMINS

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'institucional001',
#        'USER': 'postgres',
#        'PASSWORD': '1234',
#    }
#}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'institucional001',
        'USER': 'root',
        'PASSWORD': 'Cl1pp3r1234',
    }
}

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': 'institucional001.db',
#        'USER': '',
#        'PASSWORD': '',
#    }
#}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Sao_Paulo'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'pt-br'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True
USE_L10N = True

try:
    from local_settings import *
except ImportError:
    pass

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT_PATH, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_ROOT_PATH, 'estatico')
STATIC_URL = '/estatico/'

ADMIN_MEDIA_PREFIX = '/admin-media/'


# Make this unique, and don't share it with anybody.
SECRET_KEY = 'tf!fa#8$0pu3lg^f#c-02v6zhc-79p+9crte4w@@bs*j+504mx'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
)

ROOT_URLCONF = 'institucional001.urls'

TEMPLATE_DIRS = (
   os.path.join(PROJECT_ROOT_PATH,'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.comments',
    'django.contrib.flatpages',
   # 'tinymce',
   # 'flatpages_tinymce',

    
    'catalogo',
    'contato',
    'empresas',
    
)

import logging
logging.basicConfig(level=logging.DEBUG)

AUTHENTICATION_BACKENDS = (
    # this is the default backend, don't forget to include it!
    'institucional001.backends.EmailOrUsernameModelBackend',
    'django.contrib.auth.backends.ModelBackend',
    # this is what you're adding for using Twitter
#    'massivecoupon.socialregistration.auth.TwitterAuth',
    #'massivecoupon.socialregistration.auth.FacebookAuth', # Facebook
#    'massivecoupon.socialregistration.auth.OpenIDAuth', # OpenID
)