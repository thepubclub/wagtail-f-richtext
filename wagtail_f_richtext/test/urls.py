from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from wagtail import VERSION as WAGTAIL_VERSION
from wagtail.admin import urls as wagtailadmin_urls

if WAGTAIL_VERSION >= (3, 0):
    from wagtail import urls as wagtail_urls
else:
    from wagtail.core import urls as wagtail_urls

from wagtail.documents import urls as wagtaildocs_urls

urlpatterns = [
    path("django-admin/", admin.site.urls),
    path("admin/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path("", include(wagtail_urls)),
]
