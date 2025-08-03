from django.db import models
from django.contrib.auth import get_user_model
from products_app.models import Product
User=get_user_model()
# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='orders',verbose_name='کاربر')
    address=models.CharField(max_length=400,verbose_name='آدرس')
    email=models.EmailField(blank=True,null=True,verbose_name='ایمیل')
    phone=models.CharField(max_length=12,verbose_name='شماره تلفن گیرنده')
    create_at=models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ایجاد سفارش')
    is_paid=models.BooleanField(default=False,verbose_name='پرداخت')
    
    def __str__(self):
        return self.user.phone # type: ignore
    class Meta:
        verbose_name_plural="سفارشات "
        verbose_name="سفارش"
       
    
class OrderItem(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE,verbose_name='سفارش')
    product=models.ForeignKey(Product, on_delete=models.CASCADE,verbose_name='محصول')
    quantity=models.SmallIntegerField(verbose_name='تعداد')
    price=models.PositiveIntegerField(verbose_name='قیمت')
    
    def __str__(self):
        return self.order.phone
    
    class Meta:
        verbose_name_plural="اقلام سفارش داده شده "
        verbose_name="قلم"