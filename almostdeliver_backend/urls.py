from django.contrib import admin
from django.urls import path
from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    # नया रास्ता: यहाँ 'product_id' बताएगा कि कौन सा सामान खरीदा गया
    path('order/<int:product_id>/', views.place_order, name='place_order'),
]