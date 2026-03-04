from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Order
from .cart import Cart  # सुनिश्चित करें कि shop/cart.py मौजूद है

# 1. होमपेज (सारे प्रोडक्ट्स दिखाने के लिए)
def index(request):
    products = Product.objects.all()
    return render(request, 'shop/index.html', {'products': products})

# 2. कार्ट में आइटम जोड़ना
def cart_add(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    cart.add(product=product)
    return redirect('cart_detail')

# 3. कार्ट से एक आइटम हटाना
def item_clear(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    cart.remove(product)
    return redirect("cart_detail")

# 4. पूरा कार्ट खाली करना
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")

# 5. कार्ट का पेज दिखाना
def cart_detail(request):
    cart = Cart(request)
    return render(request, 'shop/cart_detail.html', {'cart': cart})

# 6. चेकआउट पेज (ऑर्डर प्लेस करने के लिए)
def checkout(request):
    cart = Cart(request)
    if request.method == "POST":
        # फॉर्म से डेटा लेना
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        city = request.POST.get('city')
        phone = request.POST.get('phone')
        total_price = cart.get_total_price()

        # ऑर्डर को डेटाबेस में सेव करना
        order = Order.objects.create(
            first_name=first_name,
            last_name=last_name,
            address=address,
            city=city,
            phone=phone,
            total_price=total_price,
            status='Pending'
        )
        
        # ऑर्डर होने के बाद कार्ट खाली कर देना
        cart.clear()
        return render(request, 'shop/order_success.html', {'order': order})

    return render(request, 'shop/checkout.html', {'cart': cart})

# 7. ऑर्डर ट्रैकिंग सिस्टम
def track_order(request):
    order = None
    error_msg = None
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        try:
            # ID से ऑर्डर ढूंढना
            order = Order.objects.get(id=order_id)
        except (Order.DoesNotExist, ValueError):
            error_msg = "माफ़ कीजिये, इस ID का कोई ऑर्डर नहीं मिला।"
            
    return render(request, 'shop/track.html', {
        'order': order, 
        'error_msg': error_msg
    })