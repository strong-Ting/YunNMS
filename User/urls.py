from django.conf.urls import url
from User import views

urlpatterns = [
    url(r'setup$', views.setup),    
    url(r'$', views.dashboard),
]
