from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .cart import Cart

# Home Page: Saare products dikhane ke liye
def index(request):
    products = Product.objects.all()
    return render(request, 'shop/index.html', {'products': products})

# Add to Cart: Ismein humne TypeError se bachne ke liye try-except lagaya hai
def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    
    # Hum yahan positional argument bhej rahe hain (product) keyword nahi (product=product)
    try:
        cart.add(
            product, 
            price=product.price, 
            name=product.name,
            image_url=product.image_url if hasattr(product, 'image_url') else ""
        )
    except TypeError:
        # Agar tumhara Cart system purana hai, toh ye bina extra info ke add karega
        cart.add(product)
        
    return redirect('cart_detail')

# Cart Page: Cart ka total aur saman dikhane ke liye
def cart_detail(request):
    cart_obj = Cart(request)
    return render(request, 'shop/cart.html', {'cart': cart_obj})