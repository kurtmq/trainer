from .settings import *

# Security settings
DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY', 'default-key-for-build')

# Allow Cloud Run URL
ALLOWED_HOSTS = ['*']  # You should restrict this in production

# Database - use Cloud SQL or another managed database
# For development/testing, use SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')