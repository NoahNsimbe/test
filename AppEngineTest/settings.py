import os
import sys
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ENVIRONMENT = os.getenv("ENVIRONMENT", "DEVELOPMENT")

DEBUG = True if ENVIRONMENT == "DEVELOPMENT" else False

if not DEBUG:
    env_path = os.path.join(os.path.dirname(__file__), '.env_prod')
    load_dotenv(env_path)

SECRET_KEY = "21b6%r1x@h2k!z_hulql=04zl)m9qt6_g)yggepr#s)=1*69=a" if DEBUG else os.getenv("SECRET_KEY")

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls.apps.PollsConfig',
    'rest_framework'
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

ROOT_URLCONF = 'AppEngineTest.urls'

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

WSGI_APPLICATION = 'AppEngineTest.wsgi.application'

if DEBUG:
    DATABASES = {
        
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '127.0.0.1',
            'USER': 'app-engine-test',
            'PASSWORD': os.getenv("DB_PASSWORD", "app-engine-test"),
            'NAME': 'app_engine_test',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'OPTIONS': {
                'init_command': 'SET default_storage_engine=INNODB',
                'sql_mode': 'STRICT_TRANS_TABLES',
                'isolation_level': 'read committed'
            },
            'HOST': os.getenv("DATABASE_HOST"),
            'USER': os.getenv("DATABASE_USER"),
            'PASSWORD': os.getenv("DATABASE_PASSWORD"),
            'NAME': os.getenv("DATABASE_NAME"),
            'PORT': os.environ.get('DATABASE_HOST_PORT'),
        }
    }
    
if 'test' in sys.argv:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test_db'
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

if DEBUG:

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.join(BASE_DIR + '/storage.json')
    DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
    GS_BUCKET_NAME = 'candidates_media'
    MEDIA_URL = 'https://storage.googleapis.com/{}/'.format(GS_BUCKET_NAME)

else:
    DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
    GS_BUCKET_NAME = 'candidates_media'
    MEDIA_URL = 'https://storage.googleapis.com/{}/'.format(GS_BUCKET_NAME)

STATIC_ROOT = 'static'
STATIC_URL = '/static/'

if not DEBUG:
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
