from django.contrib import admin

# Register your models here.
from product.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name", "hpp", "selling_price","created_date","update_date")

admin.site.register(Product, ProductAdmin)