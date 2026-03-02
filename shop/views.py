from django.shortcuts import render, redirect, get_object_or_404
from .models import Product  # पक्का करें कि आपके मॉडल का नाम Product ही है
from .cart import Cart

# 1. होमपेज (जो एरर दे रहा था)
def index(request):
    products = Product.objects.all()
    return render(request, 'shop/index.html', {'products': products})

# 2. सामान की पूरी जानकारी
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'shop/product_detail.html', {'product': product})

# 3. कार्ट में सामान जोड़ना
def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)
    return redirect('cart_detail')

# 4. कार्ट का पेज देखना
def cart_detail(request):
    cart_obj = Cart(request)
    # यहाँ हम कार्ट के अंदर के डेटा को संभालते हैं
    return render(request, 'shop/cart.html', {'cart': cart_obj})

# 5. कार्ट से सामान हटाना (Optional पर काम आएगा)
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")