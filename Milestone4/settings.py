"""
Django settings for Milestone4 project.

"""

''' import relevant files and databases. '''
import os
''' import env '''
if os.path.exists("env.py"):
    import env

''' import relevant databases. '''
import dj_database_url


''' Build paths inside the project like this: os.path.join(BASE_DIR, ...)'''
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


''' SECURITY Key '''

SECRET_KEY = os.environ.get('SECRET_KEY')


''' Debug to be turned of for production. '''

DEBUG = True


''' Allowed hosts '''

ALLOWED_HOSTS = ['localhost', 'patricks4thmilestoneproject.herokuapp.com']


''' Application definition '''

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_forms_bootstrap',
    'home',
    'accounts',
    'products',
    'cart',
    'checkout',
    'reviews',
    'storages',
]


''' Middleware needed beyond the OS. '''

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


''' Root url '''

ROOT_URLCONF = 'Milestone4.urls'


''' Django templates '''

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'cart.contexts.cart_contents'
            ],
        },
    },
]


WSGI_APPLICATION = 'Milestone4.wsgi.application'


''' Database '''

if "DATABASE_URL" in os.environ:
    DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}
else:
    print("Failed to use DATABASE_URL. Using SQlite instead.")
    DATABASES = {
                    'default': {
                                 'ENGINE': 'django.db.backends.sqlite3',
                                 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
                                }
                }


''' Password validation '''
''' https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators'''

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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'accounts.backends.CaseInsensitiveAuth'
]

''' Internationalization '''

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


''' AWS settings '''

AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Mon, 10 Jun 2080 19:00:00 GMT',
    'CacheControl': 'max-age=99999999'
}

AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = 'eu-west-1'
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

AWS_S3_HOST = 's3-eu-west-1.amazonaws.com'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME


''' Static and Media files (CSS, JavaScript, Images) '''

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIAFILES_LOCATION = 'media'
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'


STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE')
STRIPE_SECRET = os.getenv('STRIPE_SECRET')


MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

''' Email settings '''

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = '587'
EMAIL_HOST_USER = "testingdev1990@gmail.com"
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
