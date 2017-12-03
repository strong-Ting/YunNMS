import os
# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 

MONGODB_DATABASES = {
    "YunNMS": {
        "name": "NMS",
        "host": "140.125.207.240:27017",
        "username": "NMS",
        "password": "_NMS_",
        "tz_aware": True
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



