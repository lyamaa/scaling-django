ALLOWED_HOSTS = [
    "www.my-site.com"
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'your-pass',
        'HOST': 'you-required-host',
        'PORT': '5432',
    }
}
