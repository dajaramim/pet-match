"""
URL Configuration for petmatch project.
"""
from django.conf import settings
from django.urls import include, path, re_path
from django.contrib import admin

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    path('api/', include('movies.api_urls')),
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
