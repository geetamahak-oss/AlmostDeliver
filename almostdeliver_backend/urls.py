from django.contrib import admin
from django.urls import path, include  # 'include' को यहाँ जोड़ना जरूरी है
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # एडमिन पैनल के लिए
    path('admin/', admin.site.urls),
    
    # अपनी दुकान (Shop App) के सारे रास्ते यहाँ जुड़ेंगे
    path('', include('shop.urls')), 
]

# फोटो (Images) को सर्वर पर दिखाने के लिए ये लाइनें जोड़ें
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)