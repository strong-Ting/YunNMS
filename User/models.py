from django.db import models

# MongoDB Init connection.
from YunNMS import settings as NMS_settings
from mongoengine import connect
client = connect(NMS_settings.MONGODB_DATABASES['YunNMS']['host'])
db = client[NMS_settings.MONGODB_DATABASES['YunNMS']['name']]
col = db['NMS_User']

# DB access method.
def create(user):
    col.insert_one(user)

def remove(user):
    col.find(user).remove()

def find_all(user):
    return col.find(user)

def find_one(user):
    return col.find_one(user)
# Create your models here.
