from django.shortcuts import render, redirect, get_object_ some_object_or_404
from .models import Product
from .cart import Cart

# 1. Home Page View (Sare products dikhane ke liye)
def index(request):
    products = Product.objects.all()
    return render(request, 'shop/index.html', {'products': products})

# 2. Add to Cart View (Ismein humne Photo/Image URL add kiya hai)
def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    
    # Cart mein product save karte waqt uska naam, daam aur photo bhej rahe hain
    cart.add(
        product=product, 
        price=product.price, 
        name=product.name,
        image_url=product.image_url  # <-- Ye line photo dikhane ke liye zaroori hai
    )
    
    return redirect('cart_detail')

# 3. Cart Detail View (Cart ka saman dikhane ke liye)
def cart_detail(request):
    cart_obj = Cart(request)
    return render(request, 'shop/cart.html', {'cart': cart_obj})

# 4. Item Remove karne ke liye (Optional)
def item_clear(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    cart.remove(product)
    return redirect("cart_detail")

# 5. Pura Cart khali karne ke liye (Optional)
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")