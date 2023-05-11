from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from bytesofcyber import settings

urlpatterns = [
    path('', include('portfolio.urls')),
    path('admin/', admin.site.urls),
    path('bootstrap/', include('bootstrap.urls')),
    path('pfsense/', include('pfsense.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
