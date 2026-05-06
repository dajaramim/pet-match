"""
URL Configuration for petmatch project.
"""
from django.conf import settings
from django.urls import include, re_path
from django.contrib import admin

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^', include('movies.urls')),
]

# Serve media files during development
if settings.DEBUG:
    from django.views.static import serve
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
