# Django settings for htlearn project.

import os

# Current Project Directory for other paths to be relative to this.
PROJECT_DIR = os.path.dirname( __file__ )

DEBUG = True
TEMPLATE_DEBUG = DEBUG

INTERNAL_IPS = ( '127.0.0.1' )

ADMINS = ( 
    # ('Your Name', 'your_email@domain.com'),
 )

MANAGERS = ADMINS

DATABASES = {

#    'default': {
#        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#        'NAME': 'dbname', # Or path to database file if using sqlite3.
#        'USER': 'root', # Not used with sqlite3.
#        'PASSWORD': 'root', # Not used with sqlite3.
#        'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
#        'PORT': '', # Set to empty string for default. Not used with sqlite3.
    },

}
TIME_ZONE = 'Asia/Calcutta'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

ADMIN_MEDIA_PREFIX = '/admin/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '!d&6t3po&=b&cr!m$fp7yz7stweauoefa$-w8%rfo1rj4&dnkc'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = ( 
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
 )

MIDDLEWARE_CLASSES = ( 
#    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
 )

ROOT_URLCONF = 'urls'

TEMPLATE_CONTEXT_PROCESSORS = ( 
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
 )

INSTALLED_APPS = ( 
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'sqloperation'
 )
