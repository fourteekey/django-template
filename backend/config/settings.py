import os
import environ


env = environ.Env(DEBUG=(bool, False),)
environ.Env.read_env()

SETTINGS_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(SETTINGS_DIR)


SECRET_KEY = env.str('SECRET_KEY')

DEBUG = env.bool('DEBUG')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True


DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # 'whitenoise.runserver_nostatic',  # < Per Whitenoise, to disable built in
    'django.contrib.staticfiles',
    'corsheaders',
]
THIRD_APPS = [
    'rest_framework',
    'drf_yasg',
]
LOCAL_APPS = [
    'api',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_APPS + LOCAL_APPS
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',    #add whitenoise
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',        # cors to dfr
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
APPEND_SLASH = True

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
# CORS_ORIGIN_WHITELIST = ('https://127.0.0.1:8080', 'https://127.0.0.1:8000', 'https://195.69.187.126:8080')
CORS_URLS_REGEX = r'.*/api/.*$'     # сors only for API url

CSRF_TRUSTED_ORIGINS = []

# CACHES = {
#     'default':{
#         'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
#         'LOCATION': 'dataflair_cache',
#     }
# }


# AUTH_USER_MODEL = 'users.CustomUser'
ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # or 'django.template.backends.jinja2.Jinja2',
        'DIRS': [os.path.join(BASE_DIR, 'dist')],
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

WSGI_APPLICATION = 'config.wsgi.application'
SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"


DATABASES = {
    'default': env.db()
}

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


LANGUAGE_CODE = 'ru-RU'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = False
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'dist', 'static')
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'assets'))

# STATICFILES_FINDERS = (
#     'django.contrib.staticfiles.finders.FileSystemFinder',
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
# )
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'


##########
# API #
##########
REST_FRAMEWORK = {
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'rest_framework.authentication.BasicAuthentication',
    #     'rest_framework.authentication.TokenAuthentication',
    # ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DATETIME_FORMAT': ('%d.%m.%Y %H:%M:%S',)
}

# REST_AUTH_SERIALIZERS = {
#     'USER_DETAILS_SERIALIZER': 'users.serializers.CustomUserDetailsSerializer',
# }
API_URL = env.str('API_URL')

# # Fake PyMySQL's version and install as MySQLdb add to __init__
# # https://adamj.eu/tech/2020/02/04/how-to-use-pymysql-with-django/
# import pymysql
# pymysql.version_info = (1, 4, 2, "final", 0)
# pymysql.install_as_MySQLdb()
