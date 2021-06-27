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

# for s3 bucket
AWS_ACCESS_KEY_ID = "AKIA6OWLQSQFTDUDVP5A"
AWS_SECRET_ACCESS_KEY = "0ZkNmqRYROt0qA+0Ikm9ZPDZx64x9WJt0YShzBvA"
AWS_STORAGE_BUCKET_NAME = "atithighar"
AWS_DEFAULT_ACL = 'public-read'
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}

# s3 static settings
STATIC_LOCATION = 'static'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
STATICFILES_STORAGE = 'atithighar.backends.StaticStorage'

# s3 public media settings
MEDIA_LOCATION = 'media'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIA_LOCATION}/'
DEFAULT_FILE_STORAGE = 'atithighar.backends.MediaStorage'

# ses email settings
AWS_SES_ACCESS_KEY_ID = "AKIA6OWLQSQFQ2DQOYN6"
AWS_SES_SECRET_ACCESS_KEY = "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"

AWS_SES_REGION_NAME = 'ap-south-1'
AWS_SES_REGION_ENDPOINT = f'email.{AWS_SES_REGION_NAME}.amazonaws.com'

EMAIL_BACKEND = 'django_ses.SESBackend'

# production settings
CORS_REPLACE_HTTPS_REFERER = True
HOST_SCHEME = "https://"
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_SECONDS = 1000000
SECURE_HSTS_PRELOAD = True
