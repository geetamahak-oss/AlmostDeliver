from django.contrib import admin
from .models import Product, Order
from django.utils.html import format_html

# यह क्लास बताएगी कि ऑर्डर लिस्ट कैसी दिखनी चाहिए
class OrderAdmin(admin.ModelAdmin):
    # list_display में जो नाम लिखेंगे, वही एडमिन पैनल के कॉलम बनेंगे
    list_display = ('customer_name', 'product', 'phone', 'whatsapp_link')

    # यहाँ हम WhatsApp बटन बना रहे हैं
    def whatsapp_link(self, obj):
        return format_html(
            '<a style="background: #25D366; color: white; padding: 6px 12px; border-radius: 20px; text-decoration: none; font-weight: bold; font-size: 12px;" '
            'href="https://wa.me/91{}?text=नमस्ते {}, AlmostDeliver से आपका ऑर्डर मिल गया है!" target="_blank">Chat on WhatsApp</a>',
            obj.phone, obj.customer_name
        )
    whatsapp_link.short_description = 'WhatsApp Action' # कॉलम का नाम

# अब मॉडल्स को रजिस्टर करें
admin.site.register(Product)
admin.site.register(Order, OrderAdmin)