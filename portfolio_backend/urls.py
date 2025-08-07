from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/projects/', include('projects.urls')),
    path('api/contact/', include('contact.urls')),
    path('api/admin/', include('admin_auth.urls')),  # or whatever app name you use


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

