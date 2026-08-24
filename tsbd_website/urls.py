from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("website.urls")),
    path("dashboard/", include("dashboard.urls")),
    path("dashboard/products/", include("products.urls")),
    path("dashboard/blog/", include("blog.urls")),
    path('dashboard/team/',include('team.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
