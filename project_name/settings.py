"""
Django settings for {{ project_name }} project.
"""
from os.path import join, dirname, abspath
from prettyconf import config, casts
import dj_database_url
import pytz

BASE_DIR = dirname(dirname(abspath(__file__)))


# Development Settings as Defaults

DEBUG = config('DEBUG', default=True, cast=casts.Boolean)
SECRET_KEY = config('SECRET_KEY', default='{{ secret_key }}')

DEFAULT_HOST = ['*'] if DEBUG else None
DEFAULT_DB = 'sqlite:///'+join(BASE_DIR, 'db.sqlite3')

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default=DEFAULT_HOST, cast=casts.List)
DATABASE_URL = config('DATABASE_URL', default=DEFAULT_DB)

# Internationalization

LANGUAGE_CODE = config('LANGUAGE_CODE', default='en-us')
TIME_ZONE = config('TIME_ZONE', default='UTC')
USE_I18N = True
USE_L10N = True
USE_TZ = True

US_TIMEZONES = (
    (pytz.timezone('US/Eastern'), 'Eastern'),
    (pytz.timezone('US/Central'), 'Central'),
    (pytz.timezone('US/Mountain'), 'Mountain'),
    (pytz.timezone('US/Pacific'), 'Pacific'),
    (pytz.timezone('US/Arizona'), 'Arizona'),
    (pytz.timezone('US/Alaska'), 'Alaska'),
    (pytz.timezone('US/Hawaii'), 'Hawaii'),
)

# Application definition

INSTALLED_APPS = (

    'django_nose',
    'rest_framework',
)

AUTH_COOKIE_NAME = 'user'
AUTH_USER_MODEL = 'accounts.User'

MIDDLEWARE_CLASSES = (

)

ROOT_URLCONF = '{{ project_name }}.urls'
WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

USE_X_FORWARDED_HOST = True
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = [
    '--with-coverage',
    '--cover-package={{ project_name }}',
]

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': ('rest_framework.renderers.JSONRenderer',),
    'DEFAULT_PARSER_CLASSES': ('rest_framework.parsers.JSONParser',),
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',),
}


# Databases

DATABASES = {'default': dj_database_url.config(default=DATABASE_URL)}
