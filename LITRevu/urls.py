from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("feed.urls")),
    path("authentication/", include("authentication.urls")),
    path("reviews/", include("reviews.urls")),
    path("user_management/", include("user_management.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)