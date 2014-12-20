from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'users.views.users_list'),
    url(r'^login/', 'users.views.user_login'),
    url(r'^logout/', 'users.views.user_logout'),
    url(r'^user/(?P<username>[\w]+)/$', 'users.views.user_profile'),
    url(r'^user/(?P<username>[\w]+)/materials/$', 'users.views.user_pubs'),
    
)