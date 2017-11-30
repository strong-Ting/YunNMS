from django.conf.urls import url

from User import views

urlpatterns = [
#    url(r'/Delete/(?P<_id>\w+)$', views.delete),
#    url(r'/Modify/(?P<_id>\w+)$', views.modify),
    url(r'/(?P<action>\w+)/$', views.dashboard),
    url(r'/(?P<action>\w+)/(?P<id>\w+)$', views.dashboard),
    url(r'$', views.dashboard),
]
