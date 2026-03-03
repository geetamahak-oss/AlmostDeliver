from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:product_id>/', views.item_clear, name='item_clear'), # Remove के लिए
    path('checkout/', views.checkout, name='checkout'), # Checkout के लिए
]