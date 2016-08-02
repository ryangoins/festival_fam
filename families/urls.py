from django.conf.urls import include, url
from django.contrib import admin

from . import views
from . import models


urlpatterns = [
    url(r'(?P<pk>\d+)/$', views.group_detail, name='detail'),
]
