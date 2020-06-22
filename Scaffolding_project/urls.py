from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    # Uncomment the next line to enable the admin:
    path('admin/', admin.site.urls),
    path('', include('my_site.urls')),
]


if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
