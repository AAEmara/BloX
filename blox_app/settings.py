# blox_app/settings.py

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@v%_7o#582)q*!z62v-7fv8h9dfsad*2=d$(&#ub0m2b(#!c6*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'blog',
    'blog_auth',
    'comments',
    'admin_panel',
    'rest_framework',
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

ROOT_URLCONF = 'blox_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'blox_app.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/topics/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [ BASE_DIR / 'static']

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'blog_auth.CustomUser'

# --- IMPORTANT CHANGES FOR AUTHENTICATION REDIRECTS ---

# LOGIN_URL: Where @login_required decorator redirects unauthenticated users.
# Assuming your login page is at /auth/login/ and its URL name is 'login' within 'blog_auth' app.
LOGIN_URL = 'blog_auth:login'

# LOGIN_REDIRECT_URL: Where Django redirects after a successful login.
# Since 'home' is namespaced in your 'blog' app.
LOGIN_REDIRECT_URL = 'blog:home'

# LOGOUT_REDIRECT_URL: Where Django redirects after a successful logout.
# Assuming your login page is at /auth/login/ and its URL name is 'login' within 'blog_auth' app.
LOGOUT_REDIRECT_URL = 'blog_auth:login'

# --- END OF IMPORTANT CHANGES ---


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [ # Corrected 'PREMISSION_CLASSES' to 'PERMISSION_CLASSES'
        'rest_framework.permissions.IsAuthenticatedOrReadOnly', # Corrected 'premissions' to 'permissions'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ]
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'       # Gmail's SMTP server
EMAIL_PORT = 587                    # Gmail's SMTP port for TLS
EMAIL_USE_TLS = True                # Use TLS for security
# prefered to be in the .env
EMAIL_HOST_USER = 'company_gmail@gmail.com' # The gmail we want to send message from
# prefered to be in the .env
EMAIL_HOST_PASSWORD = 'your_generated_app_password' # The 16-character App Password you generated
DEFAULT_FROM_EMAIL = ' Company Name <company_gmail@gmail.com>' # How the 'From' field will appear
SERVER_EMAIL = 'errors@yourcompany.com' # For Django's internal error reporting emails
