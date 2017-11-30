from django.conf.urls import url, include

from Backend import views
from Permission import views as per_views
from Cisco import views as cis_views

urlpatterns = [
    url(r'^permission', per_views.dashboard),
    url(r'^user', include('User.urls')),
    url(r'^cisco', cis_views.dashboard),
    url(r'$', views.index),
]
