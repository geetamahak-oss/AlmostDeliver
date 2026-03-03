from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .cart import Cart

# 1. Home Page: सारे प्रोडक्ट्स दिखाने के लिए
def index(request):
    products = Product.objects.all()
    return render(request, 'shop/index.html', {'products': products})

# 2. Add to Cart: सामान को कार्ट में जोड़ने के लिए
def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    
    # Try-Except ताकि अगर cart.py अलग हो तो भी एरर न आए
    try:
        cart.add(
            product, 
            price=product.price, 
            name=product.name,
            image_url=product.image_url if hasattr(product, 'image_url') else ""
        )
    except TypeError:
        # अगर कार्ट क्लास पुराने स्टाइल की है
        cart.add(product)
        
    return redirect('cart_detail')

# 3. Cart Detail: कार्ट का सामान और टोटल देखने के लिए
def cart_detail(request):
    cart_obj = Cart(request)
    return render(request, 'shop/cart.html', {'cart': cart_obj})

# 4. Remove Item: कार्ट से एक सामान हटाने के लिए (urls.py में इसे item_clear नाम दिया है)
def item_clear(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect("cart_detail")

# 5. Checkout Page: ऑर्डर फाइनल करने का पेज
def checkout(request):
    # अभी हम सिर्फ पेज दिखा रहे हैं, बाद में यहाँ फॉर्म का डेटा लेंगे
    return render(request, 'shop/checkout.html')