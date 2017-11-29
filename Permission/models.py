from django.db import models

from YunNMS import settings as NMS_settings
from mongoengine import connect

from Permission import settings
client = connect(NMS_settings.MONGODB_DATABASES['YunNMS']['host'])
db = client[NMS_settings.MONGODB_DATABASES['YunNMS']['name']]
col = db['NMS_Permission']

# Create your models here.
#class Permission(models.Model):
#    code = models.TextField(primary_key=True)
#    name = models.TextField()
#    
#    class Meta:
#        db_table = 'NMS_Permission'
