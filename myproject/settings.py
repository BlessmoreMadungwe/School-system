from pathlib import Path
import os
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# ------------------------
# SECURITY
# ------------------------
SECRET_KEY = 'django-insecure-sz7a_bhq4sjeu@#3kjkrs#@!_(&!mps6y%76n)_obgbf^o$wv8'
DEBUG = False

# Render domain + optional localhost
ALLOWED_HOSTS = ['school-system-ywgr.onrender.com', '127.0.0.1', 'localhost']

# ------------------------
# INSTALLED APPS
# ------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Your apps
    'core',
    'dashboard',
    'students',
    'teachers',
    'departments',
    'subjects',
    'accounts',
]

# ------------------------
# MIDDLEWARE
# ------------------------
MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',  # serve static in production
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ------------------------
# TEMPLATES
# ------------------------
ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',  # allows request in templates
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'

# ------------------------
# DATABASE
# ------------------------
DATABASES = {
    'default': dj_database_url.parse(
        'postgresql://school_xp0g_user:jfUgxzamqIJGmNkS2RZj7o9Q0qjKDcjO@dpg-d76fg7hr0fns73c9c5bg-a.virginia-postgres.render.com/school_xp0g',
        conn_max_age=600, ssl_require=True
    )
}

# ------------------------
# PASSWORD VALIDATION
# ------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ------------------------
# INTERNATIONALIZATION
# ------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ------------------------
# STATIC FILES
# ------------------------
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # production collection folder
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]  # development static folder

# WhiteNoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ------------------------
# MEDIA FILES
# ------------------------
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ------------------------
# LOGIN / LOGOUT
# ------------------------
LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = 'login'