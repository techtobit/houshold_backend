
from pathlib import Path
import os
import dj_database_url
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-iv^p)@9#)y_yemi&8tia3(jg_ga6an$aqrifv^1s-5c3u#0)u3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*", "https://household-backend-a4k7.onrender.com/"]

CORS_ALLOWED_ORIGINS = [
    'https://house-hold-front-end.vercel.app',
]

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'phone_field',
    'orders',
    'services',
    'accounts'
]



REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.IsAuthenticated',
    ],
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR,'templates'],
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


WSGI_APPLICATION = 'api.wsgi.application'



# DATABASES = {
#     'default': dj_database_url.config(
#         # Replace this value with your local database's connection string.
#         default='postgresql://houshold_backend_user:hDBw4EUJ8gDYKuAF5rbxvbTXiReGgxK6@dpg-cte5guggph6c73bqbb8g-a.singapore-postgres.render.com/houshold_backend',
#         # conn_max_age=600
#     )
# }

# Add these at the top of your settings.py


DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://neondb_owner:GdeS3VzhRkj6@ep-royal-sound-a507uq72.us-east-2.aws.neon.tech/neondb?sslmode=require',
        conn_max_age=600,
        # ssl_require=True
    )
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

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


MEDIA_URL = ''

if not DEBUG:
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

