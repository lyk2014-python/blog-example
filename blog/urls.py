from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'main.views.index', name='home'),
    url(r'^post/(?P<slug>[-\w]+)$', 'main.views.post_detail', name='detail'),
    url(r'^admin/', include(admin.site.urls)),
)
