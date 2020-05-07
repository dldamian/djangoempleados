
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Incluimos URLS de app 'Departamento'
    re_path('', include('apps.departamento.urls')),
    # Incluimos URLS de app 'Personal'
    re_path('', include('apps.personal.urls')),
    # Incluimos URLS de app 'Home'
    re_path('', include('apps.home.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
