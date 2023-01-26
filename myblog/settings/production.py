from .base import *

DEBUG = False


#### pipe edit

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#### end pipe edit

try:
    from .local import *
except ImportError:
    pass
