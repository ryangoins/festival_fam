from django.conf.urls import include, url
from django.contrib import admin
from accounts.views import AddUser

from . import views
from . import models

urlpatterns = [
    url(r'^signup/$', AddUser.as_view(), name="signup"),
    #url(r'^accounts/update/(?P<slug>[\-\w]+)/$', views.UpdateProfile.as_view(), name='update_profile'),
]
