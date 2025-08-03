from django.contrib import admin
from . import models


class OrderItemAdmin(admin.TabularInline):
    model=models.OrderItem

@admin.register(models.Order)
class Order_admin(admin.ModelAdmin):
    list_display=['user','address','phone','is_paid']
    list_filter=['is_paid']
    inlines=[OrderItemAdmin,]