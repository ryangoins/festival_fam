from django.conf.urls import include, url
from django.contrib import admin

from . import views
from families.views import CreateGroup
from todo.views import view_list
from . import models

urlpatterns = [
    url(r'(?P<group_pk>\d+)/meals/(?P<meal_pk>\d+)/$', views.meal_detail, name='meal_detail'),
    url(r'(?P<group_pk>\d+)/meals/$', views.meal_list, name='meal_list'),
    url(r'(?P<group_pk>\d+)/meals/create/$', views.create_meal, name='create_meal'),
    url(r'(?P<group_pk>\d+)/$', views.group_detail, name='detail'),
    url(r'^user/(?P<username>[\w.@+-]+)/$', views.group_list, name='group_list'),
    url(r'^create/$', CreateGroup.as_view(), name='create_group'),
    #url(r'(?P<pk>\d+)/todo/(?P<list_id>\d{1,4})/(?P<list_slug>[\w-]+)/$', views.view_list, name='list_view'),
    url(r'(?P<group_pk>\d+)/todo/', include('todo.urls', namespace='todo')),
    url(r'(?P<group_pk>\d+)/festival-info/', include('festivals.urls', namespace='festivals')),

]
