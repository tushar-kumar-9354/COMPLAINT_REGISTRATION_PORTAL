import os
from pathlib import Path

# BASE DIRECTORY
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'your-secret-key'  # replace this in production

# DEVELOPMENT SETTINGS
DEBUG = True
<<<<<<< HEAD
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'complaint-registration-nnuw.onrender.com',
]
CSRF_TRUSTED_ORIGINS = [
    'https://complaint-registration-nnuw.onrender.com',
]
=======
ALLOWED_HOSTS = ['complaint-registration-portal.onrender.com']
CSRF_TRUSTED_ORIGINS = ['https://complaint-registration-portal.onrender.com']
>>>>>>> b98ec99c7db4cd0e8a1bdc85b14eba7d38906d93
# APPLICATION DEFINITIONS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'complaints',  # your app
      # optional: for better form rendering
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
<<<<<<< HEAD
    'whitenoise.middleware.WhiteNoiseMiddleware',
=======
>>>>>>> b98ec99c7db4cd0e8a1bdc85b14eba7d38906d93
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'civic_complaints.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # not using a global templates folder
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


WSGI_APPLICATION = 'civic_complaints.wsgi.application'

# ✅ DATABASE CONFIG - PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
<<<<<<< HEAD
        'NAME': 'civicdatabase',
        'USER': 'civicuser',
        'PASSWORD': 'yk43x2Uh7inOTYwRiJSgd01oF1OZKsY2',
        'HOST': 'dpg-d26a47be5dus73ddhjpg-a.oregon-postgres.render.com',
        'PORT': '5432',
        'OPTIONS': {
            'sslmode': 'require',
        }
    }
}


=======
        'NAME': 'civic_database',  # replace with your database name
        'USER': 'postgres',
        'PASSWORD': '12345',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
>>>>>>> b98ec99c7db4cd0e8a1bdc85b14eba7d38906d93
import sys
if 'test' in sys.argv:
    DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3'}
# ✅ CUSTOM USER MODEL
AUTH_USER_MODEL = 'complaints.User'


# ✅ PASSWORD VALIDATORS
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# ✅ LANGUAGE & TIMEZONE
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ✅ STATIC FILES
<<<<<<< HEAD
# settings.py

STATIC_URL = '/static/'

# Where collected static files will be placed (for production)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# (Optional, good for development)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# ✅ MEDIA FILES

=======
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# ✅ MEDIA FILES
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
>>>>>>> b98ec99c7db4cd0e8a1bdc85b14eba7d38906d93
# ✅ DEFAULT PRIMARY KEY FIELD
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ✅ LOGIN/LOGOUT REDIRECTS
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'login'
LOGIN_URL = 'login'

# ✅ Crispy Forms (optional)
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# settings.py

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 465
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

EMAIL_HOST_USER = 'jangratushar348@gmail.com'         # Your email
EMAIL_HOST_PASSWORD = 'xdycxnvblsudapog'        # App Password (not your real password!)
