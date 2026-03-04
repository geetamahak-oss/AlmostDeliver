from django.contrib import admin
from .models import Product, Order

# Product को एडमिन में दिखाने के लिए
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')

# Order को एडमिन में दिखाने के लिए (यहीं पर गलती थी)
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # list_display में वही नाम होने चाहिए जो models.py में हैं
    list_display = ('id', 'first_name', 'last_name', 'phone', 'total_price', 'status', 'created_at')
    
    # एडमिन में फिल्टर और सर्च का ऑप्शन देने के लिए
    list_filter = ('status', 'created_at')
    search_fields = ('first_name', 'phone', 'id')
    
    # एडमिन से ही स्टेटस बदलने की अनुमति देने के लिए
    list_editable = ('status',)