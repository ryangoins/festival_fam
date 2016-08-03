from django.conf.urls import include, url
from django.contrib import admin

from . import views
from . import models

urlpatterns = [
    url(r'(?P<pk>\d+)/$', views.group_detail, name='detail'),
    url(r'^user/(?P<username>[\w.@+-]+)/$', views.group_list, name='group_list'),
    url(r'^create/$', views.create_group, name='create_group'),
]
