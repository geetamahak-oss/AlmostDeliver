class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, product_id):
        p_id = str(product_id)
        if p_id not in self.cart:
            self.cart[p_id] = {'quantity': 1}
        else:
            self.cart[p_id]['quantity'] += 1
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, product_id):
        p_id = str(product_id)
        if p_id in self.cart:
            del self.cart[p_id]
            self.save()

    def clear(self):
        del self.session['cart']
        self.save()