from Cisco import settings


from YunNMS import settings as NMS_settings
from mongoengine import connect
client = connect(NMS_settings.MONGODB_DATABASES['YunNMS']['host'])
db = client[NMS_settings.MONGODB_DATABASES['YunNMS']['name']]
col = db['NMS_Cisco']


