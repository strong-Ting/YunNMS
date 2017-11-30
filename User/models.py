from django.db import models
from mongoengine import connect

# MongoDB Init connection.
from YunNMS import settings as NMS_settings
client = connect(NMS_settings.MONGODB_DATABASES['YunNMS']['host'])
db = client[NMS_settings.MONGODB_DATABASES['YunNMS']['name']]
col = db['NMS_User']

# DB access method.
def create(user):
    col.insert_one(user)

def remove(user):
    return col.remove(user)

def update(_id, user):
    return col.update(_id, user)

def find_all(user):
    return col.find(user)

def find_one(user):
    return col.find_one(user)

def not_duplicate(user):
    return True if col.find(user).count() == 0 else False
# Create your models here.
