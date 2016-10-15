from django.conf.urls import include, url
from django.contrib import admin

from . import views
from . import models

urlpatterns = [
    url(r'(?P<event_slug>[\w-]+)$', views.event_info, name='event_info'),
]
