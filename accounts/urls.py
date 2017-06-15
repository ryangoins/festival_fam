from django.conf.urls import include, url
from django.contrib import admin
from accounts.views import AddUser
from django.contrib.auth import views as auth_views

from . import views
from . import models
from accounts.forms import LoginForm

urlpatterns = [
    url(r'^signup/$', AddUser.as_view(), name="signup"),
    url(r'^login/$', auth_views.login, {'template_name': 'accounts/login.html', 'authentication_form': LoginForm}, name="login"),
    url(r'^logout/$', auth_views.logout, {'template_name': 'accounts/login.html', }, name="logout"),
    url(r'update/(?P<pk>\d+)/$', views.UpdateProfile.as_view(), name='update_profile'),
    url(r'user/(?P<username>[\w.@+-]+)/(?P<pk>\d+)/profile/$', views.ProfileDetail.as_view(), name='profile'),
]
