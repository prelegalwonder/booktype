import os.path
import sys

# DJANGO DEBUG
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# a setting to determine whether we are running on OpenShift
ON_OPENSHIFT = False
if os.environ.has_key('OPENSHIFT_REPO_DIR'):
    ON_OPENSHIFT = True

PROJECT_DIR = os.path.dirname(os.path.realpath(__file__))
OPENSHIFT_REPO_DIR=os.environ["OPENSHIFT_REPO_DIR"]

# DJANGO ADMIN
ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DEFAULT_NOTIFICATION_FILTER=u"#* !* ~* \u212c*"

# BOOKI
BOOKI_MAINTENANCE_MODE = False

BOOKI_NAME = 'Booki site'
#THIS_BOOKI_SERVER = '' # the name of the booki server (comment out to use os.environ['HTTP_HOST'])

BOOKI_ROOT = OPENSHIFT_REPO_DIR  # edit this
BOOKI_URL = ''
#BOOKI_URL = 'http://%s' % THIS_BOOKI_SERVER

# E-MAIL OPTIONS
REPORT_EMAIL_USER = 'your.email@here.com'

EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
#EMAIL_HOST_USER = 'booki@' + THIS_BOOKI_SERVER
#EMAIL_HOST_PASSWORD = ''
#EMAIL_USE_TLS = False

# BOOKI DIRECTORIES

# site_static
import booki

SITE_STATIC_ROOT = '%s/libs/booki/site_static' % BOOKI_ROOT
SITE_STATIC_URL  = '%s/site_static' % BOOKI_URL

# static
STATIC_ROOT = '%s/libs/booki/static' % BOOKI_ROOT
STATIC_URL  = '%s/static' % BOOKI_URL

# data
DATA_ROOT = os.environ['OPENSHIFT_DATA_DIR']
DATA_URL  = '%s/data' % BOOKI_URL

# profile images
PROFILE_IMAGE_UPLOAD_DIR = 'profile_images/' 

# book cover images			 
COVER_IMAGE_UPLOAD_DIR = 'cover_images/'

# obsolete
MEDIA_ROOT = DATA_ROOT
MEDIA_URL = DATA_URL

ADMIN_MEDIA_PREFIX = '%s/media/' % BOOKI_URL

# URLS
OBJAVI_URL = "http://objavi.booki.cc/objavi.cgi"
ESPRI_URL = "http://objavi.booki.cc/espri.cgi"
TWIKI_GATEWAY_URL = "http://objavi.booki.cc/booki-twiki-gateway.cgi"

# lulu.com export credentials that override Objavi settings
LULU_USER = None
LULU_PASSWORD = None
LULU_API_KEY = None

# who gets credited as publisher if not otherwise specified
DEFAULT_PUBLISHER = "Unknown"

# DATABASE STUFF
DATABASE_ENGINE = 'django.db.backends.postgresql_psycopg2'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'booktype'             # Or path to database file if using sqlite3.
DATABASE_USER = os.environ['OPENSHIFT_POSTGRESQL_DB_USERNAME']             # Not used with sqlite3.
DATABASE_PASSWORD = os.environ['OPENSHIFT_POSTGRESQL_DB_PASSWORD']         # Not used with sqlite3.
DATABASE_HOST = os.environ['OPENSHIFT_POSTGRESQL_DB_HOST']             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = os.environ['OPENSHIFT_POSTGRESQL_DB_PORT']             # Set to empty string for default. Not used with sqlite3.

# REDIS STUFF
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_PASSWORD = 'somepass'

# DJANGO STUFF

AUTH_PROFILE_MODULE='account.UserProfile'

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

gettext = lambda s: s

LANGUAGES = (
  ('hr', gettext('Hrvatski')),
  ('en-us', gettext('English')),
)


SITE_ID = 1

USE_I18N = True
USE_L10N = True

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'enc*ln*vp^o2p1p6of8ip9v5_tt6r#fh2-!-@pl0ur^6ul6e)l'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
    'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.transaction.TransactionMiddleware'
)

ROOT_URLCONF = 'booki.urls'

TEMPLATE_DIRS = (
    '%s/libs/booki/templates/' % BOOKI_ROOT,
    '%s/templates/' % os.path.dirname(booki.__file__)
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',

    'south',

    # list of booki apps
    'booki.editor',
    'booki.account',
    'booki.reader',
    'booki.portal',
    'booki.messaging',

    'sputnik'
)


# LOGGING
LOGGING = { 
   'version': 1,
  'disable_existing_loggers': False,
   'handlers': {
       'mail_admins': {
           'level': 'ERROR',
           'class': 'django.utils.log.AdminEmailHandler'
        }   
    },  
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },  
    }   
}
# LOGGING

def init_logging():
    import logging
    import logging.handlers

    logger = logging.getLogger("booki")
    logger.setLevel(logging.DEBUG)
    ch = logging.handlers.RotatingFileHandler(os.environ['OPENSHIFT_PYTHON_LOG_DIR'] + '/booki.log', maxBytes=100000, backupCount=5)
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
    logger.addHandler(ch)

logInitDone=False

if not logInitDone:
    logInitDone = True
    init_logging()

