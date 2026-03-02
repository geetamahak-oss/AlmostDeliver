from django.db import models

# यह हमारी दुकान के सामान का पक्का ढांचा है
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    old_price = models.IntegerField(default=0)
    image_url = models.TextField()
    
    # यह रही वो नई लाइन जो आपको जोड़नी है:
    # 'default="General"' का मतलब है कि पुराने सामानों में अपने आप 'General' लिखा आ जाएगा।
    category = models.CharField(max_length=100, default="General") 
    delivery_time = models.CharField(max_length=100, default="24-48 घंटों में")

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE) # कौन सा सामान?
    customer_name = models.CharField(max_length=100) # ग्राहक का नाम
    address = models.TextField() # पता
    phone = models.CharField(max_length=15) # फोन नंबर
    order_date = models.DateTimeField(auto_now_add=True) # कब खरीदा?

    def __str__(self):
        return f"Order for {self.product.name} by {self.customer_name}"