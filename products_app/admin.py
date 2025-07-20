from django.contrib import admin
from .models import Product, Category
admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=["name","base_price","final_price",'category',"discount",'stock_quantity']
    list_filter=['category',]
    list_editable=["discount","base_price"]
    search_fields=["name"]