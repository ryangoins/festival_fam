"""
Django settings for festival_fam project.

Generated by 'django-admin startproject' using Django 1.9.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

CRISPY_TEMPLATE_PACK = 'bootstrap3'

SECRET_KEY = 'z!spc_d0*a+a3n65t0$qx3dod01!#&i=pji8kb1%3t_l)e#--h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

LOGIN_REDIRECT_URL = '/' # It means home view

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'social.apps.django_app.default',
    'betterforms',
    'accounts',
    'families',
    'festivals',
    'todo',

]

INSTALLED_APPS += (
    'fluent_comments',
    'crispy_forms',
    'threadedcomments',
    'django_comments',
    'django.contrib.sites',
    'widget_tweaks',
)

FLUENT_COMMENTS_EXCLUDE_FIELDS = ('name', 'email', 'url', 'title', 'honeypot')
COMMENTS_APP = 'fluent_comments'

#SOCIAL AUTH SETTINGS

#AUTHENTICATION_BACKENDS = (
#    'social.backends.open_id.OpenIdAuth',
#    'social.backends.facebook.FacebookAppOAuth2',
#    'social.backends.facebook.FacebookOAuth2',
#    'social.backends.twitter.TwitterOAuth',
#    'social.backends.soundcloud.SoundcloudOAuth2',
#    'social.backends.spotify.SpotifyOAuth2',
#    'django.contrib.auth.backends.ModelBackend',
#)


#SOCIAL_AUTH_SOUNDCLOUD_KEY = 'ac2387c72c9db8f85470c8c215d85cb2'
#SOCIAL_AUTH_SOUNDCLOUD_SECRET = '72f07f0e5370e24e2c7f1f7eb05e509c'

#SOCIAL_AUTH_USER_MODEL = 'models.User'


#SOCIAL_AUTH_PIPELINE = (
    # Get the information we can about the user and return it in a simple
    # format to create the user instance later. On some cases the details are
    # already part of the auth response from the provider, but sometimes this
    # could hit a provider API.
#    'social.pipeline.social_auth.social_details',

    # Get the social uid from whichever service we're authing thru. The uid is
    # the unique identifier of the given user in the provider.
#    'social.pipeline.social_auth.social_uid',

    # Verifies that the current auth process is valid within the current
    # project, this is where emails and domains whitelists are applied (if
    # defined).
#    'social.pipeline.social_auth.auth_allowed',

    # Checks if the current social-account is already associated in the site.
#    'social.pipeline.social_auth.social_user',

    # Make up a username for this person, appends a random string at the end if
    # there's any collision.
#    'social.pipeline.user.get_username',

    # Send a validation email to the user to verify its email address.
    # Disabled by default.
    # 'social.pipeline.mail.mail_validation',

    # Associates the current social details with another user account with
    # a similar email address. Disabled by default.
    # 'social.pipeline.social_auth.associate_by_email',

    # Create a user account if we haven't found one yet.
#    'social.pipeline.user.create_user',

    # Create the record that associated the social account with this user.
#    'social.pipeline.social_auth.associate_user',

    # Populate the extra_data field in the social record with the values
    # specified by settings (and the default ones like access_token, etc).
#    'social.pipeline.social_auth.load_extra_data',

    # Update the user record with any changed info from the auth service.
#    'social.pipeline.user.user_details',
#)
MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'festival_fam.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates',],
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

WSGI_APPLICATION = 'festival_fam.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

SITE_ID = 1

# Restrict access to todo lists/views to `is_staff()` users.
# False here falls back to `is_authenticated()` users.
TODO_STAFF_ONLY = False

# If you use the "public" ticket filing option, to whom should these tickets be assigned?
# Must be a valid username in your system. If unset, unassigned tickets go to "Anyone."
TODO_DEFAULT_ASSIGNEE = 'johndoe'

# If you use the "public" ticket filing option, to which list should these tickets be saved?
# Defaults to first list found, which is probably not what you want!
TODO_DEFAULT_LIST_ID = 23

# If you use the "public" ticket filing option, to which *named URL* should the user be
# redirected after submitting? (since they can't see the rest of the ticket system).
# Defaults to "/"
TODO_PUBLIC_SUBMIT_REDIRECT = 'dashboard'

MEDIA_ROOT = (
    os.path.join(BASE_DIR, 'media')
)
MEDIA_URL = '/media/'

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
