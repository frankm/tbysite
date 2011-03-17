from django.conf import settings
from django.conf.urls.defaults import patterns, include, \
    url
from django.contrib import admin
from django import forms
from joinform import views, forms
from django.views.generic.simple import direct_to_template

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^jsi18n/(?P<packages>\S+?)/$', 'django.views.i18n.javascript_catalog'),
    (r'^join-form/$', views.join),
   # (r'^calendars_test/', include('schedule.urls')),
    (r'^upload/cantor/$', 'upload.views.cantor_documents'),
    (r'^photologue/', include('photologue.urls')),
    #url(r'^calendar_app$', direct_to_template,{"template":"homepage_schedule.html"}),
)

if settings.DEBUG:
    urlpatterns+= patterns('',
        url(r'^media/cms/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.CMS_MEDIA_ROOT, 'show_indexes': True}),
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True})
    )

urlpatterns += patterns('',
    url(r'^', include('cms.urls')),
)
