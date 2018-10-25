from .base import *

INSTALLED_APPS += [
    'debug_toolbar',
]


MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'newbooktest', 
        'USER': 'root', 
        'PASSWORD': '', 
        'HOST': 'localhost',
        'PORT': '3306',
        'ATOMIC_REQUESTS' : True,
        'OPTIONS': {
            'sql_mode' : 'TRADITIONAL,NO_AUTO_VALUE_ON_ZERO',
        },
        'TEST': {
            'NAME': 'test_sample'
        }
    }
}