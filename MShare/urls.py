from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic.base import RedirectView
import sharing.urls
import users.urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MShare.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    (r'^tinymce/', include('tinymce.urls')),
    #url(r'^$', RedirectView.as_view(url='/materials/', permanent=False)),
    url(r'^$', 'MShare.views.index'),
    url(r'^index/$', 'MShare.views.index'),
    url(r'^materials/', include(sharing.urls)),
    url(r'^users/', include(users.urls)),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^media/(?P<path>.*)$','django.views.static.serve',
    #{'document_root': settings.MEDIA_ROOT}),
)
