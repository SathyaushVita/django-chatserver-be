from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-^ha21r(u@l^=d)10pbph&_7g^0_8@p843!9_74@%)z8=u^)y6d"
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['cs-apiserver01.sts.com']
# ALLOWED_HOSTS = [ ]


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# Application definition
INSTALLED_APPS = [
    "daphne",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'rest_framework',
    'drf_yasg',
    "channels",
    "chat",
    "corsheaders"
]
CORS_ALLOW_ALL_ORIGINS = True
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
ROOT_URLCONF = "backend.urls"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
ASGI_APPLICATION = 'backend.asgi.application'
WSGI_APPLICATION = "backend.wsgi.application"
# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }
# DATABASES = {
#     'default': {  # chat_server is the default
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'chat_server',
#         'USER': 'system',
#         'PASSWORD': 'Vishnu@143$',
#         'HOST': 'db-sathayush-prd.mysql.database.azure.com',
#         'PORT': '3306',
#         'OPTIONS': {
#             'charset': 'utf8mb4',
#         },
#     },
#     'gramadevata_updated1': {  # Separate database
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'gramadevata_updated1',
#         'USER': 'system',
#         'PASSWORD': 'Vishnu@143$',
#         'HOST': 'db-sathayush-prd.mysql.database.azure.com',
#         'PORT': '3306',
#     }
# }
import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()
# DATABASES = {
#     'default': {
#         'ENGINE': os.getenv('DB_ENGINE', 'django.db.backends.mysql'),
#         'NAME': os.getenv('DB_NAME'),
#         'USER': os.getenv('DB_USER'),
#         'PASSWORD': os.getenv('DB_PASSWORD'),
#         'HOST': os.getenv('DB_HOST'),
#         'PORT': os.getenv('DB_PORT'),
#         'OPTIONS': {
#             'charset': os.getenv('DB_OPTIONS_CHARSET', 'utf8mb4'),
#         },
#     },
#     'gramadevata_updated1': {
#         'ENGINE': os.getenv('DB_ENGINE', 'django.db.backends.mysql'),
#         'NAME': os.getenv('DB2_NAME'),
#         'USER': os.getenv('DB2_USER'),
#         'PASSWORD': os.getenv('DB2_PASSWORD'),
#         'HOST': os.getenv('DB2_HOST'),
#         'PORT': os.getenv('DB2_PORT'),
#     }
# }
from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
    'ENGINE': os.getenv('DB_ENGINE', 'django.db.backends.mysql'),
    'NAME': os.getenv('DB_NAME'),
    'USER': os.getenv('DB_USER'),
    'PASSWORD': os.getenv('DB_PASSWORD'),
    'HOST': os.getenv('DB_HOST'),
    'PORT': os.getenv('DB_PORT'),
    'OPTIONS': {
    'charset': 'utf8mb4',
    'ssl': {
    'ca': os.path.join(BASE_DIR, 'certs', 'BaltimoreCyberTrustRoot.crt.pem'),
    }
    },
    },

    'gramadevata_updated1': {
    'ENGINE': os.getenv('DB_ENGINE', 'django.db.backends.mysql'),
    'NAME': os.getenv('DB2_NAME'),
    'USER': os.getenv('DB2_USER'),
    'PASSWORD': os.getenv('DB2_PASSWORD'),
    'HOST': os.getenv('DB2_HOST'),
    'PORT': os.getenv('DB2_PORT'),
    'OPTIONS': {
    'charset': 'utf8mb4',
    'ssl': {
    'ca': os.path.join(BASE_DIR, 'certs', 'BaltimoreCyberTrustRoot.crt.pem'),
    }
    },
    }
    }

DATABASE_ROUTERS = ['backend.db_routers.RegisterRouter']
# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]
# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header',
        }
    }
}
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
STATIC_URL = "static/"
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
# CHANNEL_LAYERS = {"default": {"BACKEND": "channels.layers.InMemoryChannelLayer"}}
#CACHE_PWD = os.environ.get("CACHE_PWD", "root")
#CACHE_HOST = os.environ.get("CACHE_HOST", "localhost")
#CACHE_PORT = os.environ.get("CACHE_PORT", "6379")
#CHANNEL_LAYERS = {
#    "default": {
#        "BACKEND": "channels_redis.core.RedisChannelLayer",
#        "CONFIG": {
#            # "hosts": [(f"redis://:{CACHE_PWD}@{CACHE_HOST}:{CACHE_PORT}")]
#            "hosts": [("127.0.0.1", 6379)],
#        }
#    },
#}
CACHE_PWD = os.environ.get("CACHE_PWD", "root")
CACHE_HOST = os.environ.get("CACHE_HOST", "localhost")
CACHE_PORT = int(os.environ.get("CACHE_PORT", 6379))
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [f"redis://:{CACHE_PWD}@{CACHE_HOST}:{CACHE_PORT}"],
        },
    },
}
FILE_URL = os.getenv('File_path')
AZURE_STORAGE_CONNECTION_STRING = os.getenv('AZURE_CONNECTION_STRING')
AZURE_CONTAINER_NAME = os.getenv('AZURE_CONTAINER_NAME')
AZURE_ACCOUNT_NAME = os.getenv('AZURE_ACCOUNT_NAME')
