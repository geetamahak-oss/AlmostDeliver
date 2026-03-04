from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image_url = models.URLField(max_length=500)

    def __str__(self):
        return self.name

class Order(models.Model):
    # Status ke options jo Admin panel mein dropdown bankar aayenge
    STATUS_CHOICES = (
        ('Pending', 'Pending - Order mil gaya hai'),
        ('Packed', 'Packed - Pack ho gaya hai'),
        ('Shipped', 'Shipped - Lucknow se nikal gaya hai'),
        ('Delivered', 'Delivered - Pahunch gaya!'),
        ('Cancelled', 'Cancelled - Cancel ho gaya'),
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(default="example@gmail.com")
    address = models.TextField()
    city = models.CharField(max_length=100, default="Lucknow")
    phone = models.CharField(max_length=15)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Tracking Status Line
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.first_name} ({self.status})"