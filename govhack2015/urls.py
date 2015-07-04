from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^govhack2015/', include('ezrego.urls')),
    #url(r'^admin/', include(admin.site.urls)),
)
