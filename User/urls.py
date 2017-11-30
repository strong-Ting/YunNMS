from django.conf.urls import url

from User import views

urlpatterns = [
    url(r'/A_(?P<action>\w+)I_(?P<id>\w+)/$', views.dashboard),
    url(r'/A_(?P<action>\w+)/$', views.dashboard),
    url(r'$', views.dashboard),
]
