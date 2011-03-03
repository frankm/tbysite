# -*- coding: utf-8 -*-
import os
gettext = lambda s: s
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#        'NAME': 'db.sqlite',                      # Or path to database file if using sqlite3.
#    }
#
DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = 'cms.sqlite'

TIME_ZONE = 'America/Los_Angeles'
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'jointemplebatyahm@gmail.com'
EMAIL_HOST_PASSWORD = 'hashrocket'
EMAIL_PORT = 587
SITE_ID = 1

CMS_MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media/cms/')
MEDIA_ROOT = os.path.join(PROJECT_PATH, "media")
MEDIA_URL = "/media/"
ADMIN_MEDIA_PREFIX="/media/admin/"

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'o5#eays-bi25vf9klb**^0gxkijhxp4-b4u0i(4@hj$1l-uprl'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.media.PlaceholderMediaMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'cms.context_processors.media',
    
   # 'django.core.context_processors.csrf',

)

ROOT_URLCONF = 'tbysite.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, "templates")
)

CMS_TEMPLATES = (
    ('template_1.html', 'Template One'),
    ('template_2.html', 'Template Two'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    
    'cms',
    'mptt',
    'menus',
    'south',
    'appmedia',
    
    'cms.plugins.file',
    'cms.plugins.flash',
    'cms.plugins.googlemap',
    'cms.plugins.link',
    'cms.plugins.picture',
    'cms.plugins.snippet',
    'cms.plugins.teaser',
    'cms.plugins.text',
    'cms.plugins.video',
    'cms.plugins.twitter',

    'publisher',

     'django.contrib.admin',
    'joinform',
    'schedule',
    'upload',
    'photologue',
    
)

LANGUAGES = [
    ('en', 'English'),
]

CMS_TEMPLATES = (
    ('tby_home.html', gettext('tby base layout')),
    ('gallery_archive.html', gettext('gallery form')),
)

CMS_REDIRECTS = True

