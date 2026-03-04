from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from shop import views  # Shop views ko import kiya

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Tracking page ko priority di gayi hai
    path('track/', views.track_order, name='track_order'),
    
    # Baki saari shop ki URLs
    path('', include('shop.urls')),
]

# Static aur Media files settings
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)