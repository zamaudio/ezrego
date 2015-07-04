from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'sellvehicle$', views.sellerintent, name='sellerintent'),
    url(r'buyavehicle$', views.buyavehicle, name='buyavehicle'),
    #url(r'(?P<eventid>[0-9]+)/event$', views.event, name='event'),
    #url(r'(?P<dn>[0-9a-zA-Z]+)/profile$', views.profile, name='profile'),
    #url(r'loginv$', views.loginv, name='loginv'),
    #url(r'logoutv$', views.logoutv, name='logoutv'),
]
