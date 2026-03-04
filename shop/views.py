from django.shortcuts import render, redirect
from .models import Product, Order
from .cart import Cart

def index(request):
    products = Product.objects.all()
    return render(request, 'shop/index.html', {'products': products})

def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product, price=product.price, name=product.name, image_url=product.image_url)
    return redirect("index")

def cart_detail(request):
    return render(request, 'shop/cart.html')

def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")

def checkout(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        phone = request.POST.get('phone')
        
        # Cart ka total nikalne ke liye
        cart = Cart(request)
        total_price = cart.get_total_price()

        # Database mein order save karna
        order = Order(
            first_name=first_name,
            last_name=last_name,
            email=email,
            address=address,
            city=city,
            phone=phone,
            total_price=total_price,
            status='Pending' # Shuruat mein pending rahega
        )
        order.save()

        # Cart saaf karna order ke baad
        cart.clear()

        # Order ID ke saath success page ya WhatsApp par bhejna
        return render(request, 'shop/checkout.html', {'order_id': order.id, 'success': True})

    return render(request, 'shop/checkout.html')

# --- NAYA TRACKING FUNCTION ---
def track_order(request):
    status_data = None
    order_obj = None
    order_id = request.GET.get('order_id')
    
    if order_id:
        try:
            # Database se order id dhoondhna
            order_obj = Order.objects.get(id=order_id)
            status_data = order_obj.status
        except (Order.DoesNotExist, ValueError):
            status_data = "Invalid"

    return render(request, 'shop/track.html', {
        'status': status_data, 
        'order': order_obj,
        'order_id': order_id
    })