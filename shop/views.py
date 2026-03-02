from django.shortcuts import render, redirect
from .models import Product, Order

def home(request):
    query = request.GET.get('search')
    category = request.GET.get('cat') # यहाँ हम कैटेगरी का नाम पकड़ रहे हैं
    
    products = Product.objects.all()

    # अगर सर्च किया गया है
    if query:
        products = products.filter(name__icontains=query)
    
    # अगर कैटेगरी पर क्लिक किया गया है
    if category:
        products = products.filter(category=category)
        
    return render(request, 'shop/index.html', {'products': products})

def place_order(request, product_id):
    product = Product.objects.get(id=product_id)
    
    if request.method == "POST":
        # फॉर्म से डेटा निकालना
        name = request.POST.get('customer_name')
        addr = request.POST.get('address')
        ph = request.POST.get('phone')
        
        # डेटाबेस में ऑर्डर सेव करना
        Order.objects.create(
            product=product,
            customer_name=name,
            address=addr,
            phone=ph
        )
        # पुराना return render हटाकर यह नया वाला डालें:
        return render(request, 'shop/success.html', {
            'customer_name': name,
            'product_name': product.name
        })
    
    # अगर पहली बार पेज खोल रहे हैं (GET request), तो फॉर्म दिखाओ
    return render(request, 'shop/order_form.html', {'product': product})