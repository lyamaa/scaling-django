ALLOWED_HOSTS = [
    "www.my-site.com"
]

DATABASES = {
    'default': {
        'ENGINE': '"django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'your-pass',
        'HOST': 'you-required-host',
        'PORT': '5432',
    }
}


# production settings
CORS_REPLACE_HTTPS_REFERER = True
HOST_SCHEME = "https://"
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_SECONDS = 1000000
SECURE_HSTS_PRELOAD = True
