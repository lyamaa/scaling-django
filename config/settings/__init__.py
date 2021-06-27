
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if DEBUG:
    from .dev import *
else:
    from .prod import *
