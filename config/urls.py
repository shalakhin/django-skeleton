from django.conf.urls import url
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin

admin.site.site_header = settings.ADMIN_SITE_HEADER

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

