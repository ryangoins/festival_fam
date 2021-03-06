from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^blog/comments/', include('fluent_comments.urls')),
    url(r'^families/', include('families.urls', namespace='families')),
    #url(r'^todo/', include('todo.urls', namespace='todo')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
