from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('add-to-cart/<int:id>/', views.cart_add, name='add_to_cart'),
    path('item-clear/<int:id>/', views.item_clear, name='item_clear'),
    path('checkout/', views.checkout, name='checkout'),
]