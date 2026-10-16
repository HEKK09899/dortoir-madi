"""
URLs racine du projet Dortoir 3.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "DORTOIR MADI — Administration"
admin.site.site_title = "DORTOIR MADI"
admin.site.index_title = "Gestion de DORTOIR MADI"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('comptes.urls')),
    path("vitrine/", include("vitrine.urls")),
]

if settings.DEBUG and settings.MEDIA_ROOT:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
