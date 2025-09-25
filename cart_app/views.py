from django.shortcuts import get_object_or_404, render,redirect
from django.views import View
from products_app.models import Product
from .cart import Cart
from django.contrib import messages
from .models import Order,OrderItem
# Create your views here.
class CartDetaleView(View):
    def get(self,requst):
        cart=Cart(requst)
        return render(requst,"cart_app/cart.html",context={'cart':cart})
    
    
    
class CartAddView(View):
    def post(self,requst,id):
        product=get_object_or_404(Product,id=id)
        quntity = requst.POST.get("quntity")
        
        cart=Cart(requst)
        cart.add(product,quntity=quntity,override_quantity=True)
        messages.success(requst, f'تعداد {quntity} {product} به سبد خرید اضافه شد.')
        referer = requst.META.get('HTTP_REFERER')
        if referer:
            return redirect(referer)

        return redirect("home_app:home")
    
def cart_clear(requst):
    cart=Cart(requst)
    cart.clear()
    return redirect("cart_app:cart_detale")


def cart_remove(requst,id):
    print(id)
    cart=Cart(requst)
    cart.remove(id)
    return redirect("cart_app:cart_detale")


class OrderCreation(View):
    def get(self,requst):
        cart=Cart(requst)
        if cart.total()==0:
            messages.error(requst, f'محصولی برای خرید موجود نمی باشد.')
            return redirect("cart_app:cart_detale")
        order=Order.objects.create(user=requst.user,total=cart.total())
        for ithem in cart:
            OrderItem.objects.create(order=order,product=ithem['product'],quantity=ithem['quntity'],price=ithem['final_price'])
        cart.clear()
        return redirect("cart_app:order_detale",order.id) # type: ignore
        

class OrderDetale(View):
    def get(self,requst,pk):
        order=get_object_or_404(Order,id=pk)
        return render(requst,'cart_app/order_detale.html',context={'order':order})