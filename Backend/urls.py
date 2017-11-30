from django.conf.urls import url, include

from Backend import views
from Permission import views as per_views
from Cisco import views as cis_views

urlpatterns = [
    url(r'^permission', include('Permission.urls')),
    url(r'^user', include('User.urls')),
    url(r'^cisco', include('Cisco.urls')),
    url(r'$', views.index),
]
