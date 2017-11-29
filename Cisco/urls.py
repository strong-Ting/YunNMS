from django.conf.urls import url

from Cisco import views

urlpatterns = [
    url(r'setup$', views.setup),
    url(r'$', views.dashboard),
]
