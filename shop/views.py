from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Order
from .cart import Cart 

# 1. होमपेज (सारे पापड़ और प्रोडक्ट्स यहाँ दिखेंगे)
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

# 5. कार्ट का पेज दिखाना (यहाँ हमने फाइल का नाम cart.html रखा है)
def cart_detail(request):
    cart = Cart(request)
    return render(request, 'shop/cart.html', {'cart': cart})

# 6. चेकआउट और ऑर्डर सेव करना
def checkout(request):
    cart = Cart(request)
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        city = request.POST.get('city')
        phone = request.POST.get('phone')
        total_price = cart.get_total_price()

        # नया ऑर्डर बनाना
        order = Order.objects.create(
            first_name=first_name,
            last_name=last_name,
            address=address,
            city=city,
            phone=phone,
            total_price=total_price,
            status='Pending'
        )
        
        cart.clear() # ऑर्डर के बाद कार्ट साफ़
        return render(request, 'shop/order_success.html', {'order': order})

    return render(request, 'shop/checkout.html', {'cart': cart})

# 7. ट्रैकिंग सिस्टम
def track_order(request):
    order = None
    error_msg = None
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        try:
            order = Order.objects.get(id=order_id)
        except (Order.DoesNotExist, ValueError):
            error_msg = "माफ़ कीजिये, इस ID का कोई ऑर्डर नहीं मिला।"
            
    return render(request, 'shop/track.html', {
        'order': order, 
        'error_msg': error_msg
    })