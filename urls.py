from django.conf.urls.defaults import patterns, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import settings
from django.contrib import admin
from filebrowser.sites import site
admin.autodiscover()

handler500 = 'kupiaudit.catalog.views.internal_error'

urlpatterns = patterns('',
    (r'^cabinet', include('kupiaudit.cabinet.urls')),
    (r'^', include('kupiaudit.main.urls')),
    (r'^admin/filebrowser/', include(site.urls)),
    (r'^admin/', include(admin.site.urls)),
    (r'^tinymce/', include('tinymce.urls')),
    (r'^grappelli/', include('grappelli.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns ('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': settings.MEDIA_ROOT}),
    )

urlpatterns += staticfiles_urlpatterns()
