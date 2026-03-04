from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from shop import views  # Shop app के views को यहाँ इम्पोर्ट किया

urlpatterns = [
    # 1. एडमिन पैनल
    path('admin/', admin.site.urls),
    
    # 2. दुकान के मुख्य पेज (Home, Cart, Checkout)
    path('', include('shop.urls')), 
    
    # 3. ऑर्डर ट्रैकिंग (इसे सीधा यहीं रखा है ताकि /track/ खुले)
    path('track/', views.track_order, name='track_order'),
]

# फोटो (Images) दिखाने के लिए सेटिंग्स
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)