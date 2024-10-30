"""
Django settings for BulletinBoard project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
import os
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+a6q2e(2#tc#ne&9#ku^)6@e9@(t1f)o=(w^v31f-ol9s3ae!4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'BulletinBoard.apps.BulletinBoardConfig',  # my application
    'users.apps.UsersConfig',  # my application
    'crispy_forms',
    'crispy_bootstrap4',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django_apscheduler',  # django_apscheduler
    'django_filters',
    'django_extensions',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',

    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF = 'BulletinBoard.urls'

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
                # `allauth` needs this from django
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'BulletinBoard.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]
# pip install django-crispy-forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'





# authorisation/authentification

# allauth application
INSTALLED_APPS += [
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]
SITE_ID = 1


AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# redirect authenticated users to LOGIN_REDIRECT_URL if True
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True
# redirect user to a home page after logging in
LOGIN_REDIRECT_URL = 'home'


ACCOUNT_AUTHENTIFICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
# True позволит избежать дополнительных действий и активирует аккаунт сразу, как только мы перейдем по ссылке
# False попросит подтвердить ещё раз на сайте после прохождения по ссылке
ACCOUNT_CONFIRM_EMAIL_ON_GET = True


# подтверждение аккаунта через письмо на почту
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

ACCOUNT_UNIQUE_EMAIL = True

# тема письма для подтверждения регистрации
ACCOUNT_EMAIL_SUBJECT_PREFIX = "From Bulat with regards. "
# поле username необязательно
ACCOUNT_USERNAME_REQUIRED = False

# количество дней, в течение которых будет доступна ссылка на подтверждение регистрации
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = 'profile'
# чтобы allauth выполнил именно эту форму при регистрации пользователя,
# а не ту, что по умолчанию, напишем:
ACCOUNT_FORMS = {'/accounts/signup': 'users.forms.UserUpdateForm'}


# a user will get confirmation e-mails from the following adress
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("PASSWORD")
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = os.getenv("EMAIL")


# если пользователь вышел, его перенаправит на страницу:
LOGOUT_REDIRECT_URL = 'login'

# redirect user to a login page if he wants to access to a login required page
LOGIN_URL = '/accounts/login/' # url pattern name



"""DJANGO APPSCHEDULER"""
# date format for apscheduler
APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"
# when timeout is up, the task will be taken away
APSCHEDULER_RUN_NOW_TIMEOUT = 25  # seconds

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')