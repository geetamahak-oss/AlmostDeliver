from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .cart import Cart

# 1. Home Page: Saare products dikhane ke liye
def index(request):
    products = Product.objects.all()
    return render(request, 'shop/index.html', {'products': products})

# 2. Add to Cart: Product ko cart mein image ke saath add karne ke liye
def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    
    # Try-Except block taaki positional/keyword argument ka error na aaye
    try:
        cart.add(
            product, 
            price=product.price, 
            name=product.name,
            image_url=product.image_url if hasattr(product, 'image_url') else ""
        )
    except TypeError:
        # Agar purana cart.py hai toh sirf product bhejega
        cart.add(product)
        
    return redirect('cart_detail')

# 3. Cart Detail: Cart ka saaman aur total dikhane ke liye
def cart_detail(request):
    cart_obj = Cart(request)
    return render(request, 'shop/cart.html', {'cart': cart_obj})

# 4. Remove Item: Cart se kisi ek item ko hatane ke liye
def item_clear(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect("cart_detail")

# 5. Checkout Page: Delivery details bharne wala page
def checkout(request):
    # Yahan 'cart' bhej rahe hain taaki checkout page par total dikh sake
    cart_obj = Cart(request)
    return render(request, 'shop/checkout.html', {'cart': cart_obj})

# 6. Clear Full Cart (Optional): Pura cart khali karne ke liye
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")