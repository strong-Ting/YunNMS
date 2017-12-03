from django.db import models
from mongoengine import connect

# MongoDB Init connection.
from YunNMS import settings as NMS_settings
client = connect(NMS_settings.MONGODB_DATABASES['YunNMS']['host'])
db = client[NMS_settings.MONGODB_DATABASES['YunNMS']['name']]
col = db['NMS_User']

# CreateReadUdapteDelete
action = {
    "account": { "C": "unique", "R": None, "U": "unique", "D": None },
    'email': { "C": "unique", "R": None, "U": "unique", "D": None }
}

# DB access method.
def insert(user):
    col.insert_one(user)

def insert_many(users):
    col.insert_many(users)

def remove(user):
    return col.remove(user)

def update(_id, user):
    return col.update(_id, user)

def find_all(user):
    return col.find(user)

def find_one(user):
    return col.find_one(user)

def not_duplicate(user, incSelf=False):
    count = col.find(user).count()
    return True if count <= (1 if incSelf else 0) else False
# Create your models here.
