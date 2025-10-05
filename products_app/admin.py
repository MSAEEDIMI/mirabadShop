from django.contrib import admin
from .models import Product, Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=["name","base_price","final_price",'category',"discount",'stock_quantity']
    list_filter=['category',]
    list_editable=["discount","base_price"]
    search_fields=["name"]
    
    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','slug','parent']
    list_filter=['name',]
    prepopulated_fields={"slug":['name',]}