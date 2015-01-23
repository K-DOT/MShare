from django.conf.urls import patterns, include, url
from django.contrib import admin
from taggit.models import Tag
from sharing.models import Material, Category
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MShare.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'sharing.views.objects_list', {'model': Material}, name='materials'),
    url(r'^(\d{4})/(\w+)/(\d{2})/(?P<material>.*?)/$', 'sharing.views.material'),
    url(r'^add/$', 'sharing.views.add_material'),
    url(r'^categories/$', 'sharing.views.objects_list', {'model': Category}),
    url(r'^categories/(?P<category>\w+)/$', 'sharing.views.category'),
    url(r'^tags/$', 'sharing.views.objects_list', {'model': Tag}),
    url(r'^tags/(?P<slug>\w+)/$', 'sharing.views.tag', name='tags'),
)
