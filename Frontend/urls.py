from django.conf.urls import url

from Frontend import views

urlpatterns = [
    url('$', views.index)
]
