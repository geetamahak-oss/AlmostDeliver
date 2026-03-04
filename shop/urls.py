from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cart/', views.cart_detail, name='cart_detail'),
    
    # ध्यान दें: यहाँ 'cart_add' फंक्शन का इस्तेमाल हुआ है जो views.py में है
    path('add-to-cart/<int:id>/', views.cart_add, name='add_to_cart'),
    
    path('item-clear/<int:id>/', views.item_clear, name='item_clear'),
    path('checkout/', views.checkout, name='checkout'),
]