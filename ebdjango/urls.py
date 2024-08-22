from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from homepage.views import home  # Add this line

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Add this line
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)