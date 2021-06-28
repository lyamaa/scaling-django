import os
from config.settings import BASE_DIR

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE"),
        "ATOMIC_REQUESTS": True,
        "NAME": os.environ.get("SQL_DATABASE"),
        "USER": os.environ.get("SQL_USER"),
        "PASSWORD": os.environ.get("SQL_PASSWORD"),
        "HOST": os.environ.get("SQL_HOST"),
        "PORT": os.environ.get("SQL_PORT"),
    }
}


STATIC_URL = "/staticfiles/"
STATIC_ROOT = os.path.join(BASE_DIR.parent, "staticfiles")

MEDIA_URL = "/mediafiles/"
MEDIA_ROOT = os.path.join(BASE_DIR.parent, "mediafiles")
