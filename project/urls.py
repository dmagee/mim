from django.conf.urls import include, url
from django.contrib import admin

from welcome.views import index, health

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index),
    url(r'^health$', health),
]

urlpatterns += staticfiles_urlpatterns()
