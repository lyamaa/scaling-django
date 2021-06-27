from config.settings import BASE_DIR

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "ATOMIC_REQUESTS": True,
        "NAME": "scale",
        "USER": "scale",
        "PASSWORD": "scale",
        "HOST": "localhost",
        "PORT": "5432",
    }
}


STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR.parent / "staticfiles"  # for collect static

MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "/media/"
