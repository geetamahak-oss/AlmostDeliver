class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, product, price, name, image_url=""):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'product_id': product_id, # Yeh line ID error fix karegi
                'name': name,
                'price': str(price),
                'quantity': 1,
                'image_url': image_url,
                'total': str(price)
            }
        else:
            self.cart[product_id]['quantity'] += 1
            self.cart[product_id]['total'] = str(float(self.cart[product_id]['price']) * self.cart[product_id]['quantity'])
        
        self.save()

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def get_total_price(self):
        # Saare items ka total price calculate karne ke liye
        return sum(float(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session['cart']
        self.save()

    def save(self):
        self.session.modified = True