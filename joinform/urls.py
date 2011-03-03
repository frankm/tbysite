from django.conf import settings
from django.conf.urls.defaults import patterns, include, \
    url
from django.contrib import admin
from django import forms

from django.views.generic.simple import direct_to_template

admin.autodiscover()

urlpatterns = patterns('joinform.views',
    (r'^admin/', include(admin.site.urls)),
    
    (r'^$', 'join'),
    

    #url(r'^calendar_app$', direct_to_template,{"template":"homepage_schedule.html"}),

    #(r'^search/$', views.search),
    # just for testing - native way to sampleapp urls 
    # (r'^sampleapp-native/', include('sampleapp.urls')),
    #url(r'^$', direct_to_template,{"template":"homepage_schedule.html"}),
    
)

if settings.DEBUG:
    urlpatterns+= patterns('',
        url(r'^media/cms/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.CMS_MEDIA_ROOT, 'show_indexes': True}),
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True})
    )

urlpatterns += patterns('',
    url(r'^', include('cms.urls')),
)
