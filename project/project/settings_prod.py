from .settings import *

# Security settings
DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY', 'default-key-for-build')

# Allow Cloud Run URL
ALLOWED_HOSTS = ['*']  

# Database - use SQLite for simplicity
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')