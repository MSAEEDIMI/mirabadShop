from django.shortcuts import get_object_or_404, render,redirect
from django.views import View
from products_app.models import Product
from .cart import Cart
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

        return redirect("cart_app:cart_detale")