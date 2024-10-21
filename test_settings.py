"""
These settings are here to use during tests, because django requires them.
In a real-world use case, apps in this project are installed into other
Django applications, so these settings will not be used.
"""

SECRET_KEY = 'insecure-secret-key'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'default.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.redirects',
    'django.contrib.sites',
    'django_view_permissions',
]

ALLOWED_HOSTS = [
    'example.org',
]

ROOT_URLCONF = 'django_view_permissions.tests.test_app.urls'

SECRET_KEY = 'insecure-secret-key'

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_view_permissions.middleware.DjangoViewPermissionsMiddleware',
)
