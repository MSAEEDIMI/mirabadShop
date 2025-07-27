from django.shortcuts import render
from django.views import View
# Create your views here.
class CartView(View):
    def get(self,requst,*args, **kwargs):
        return render(requst,"cart_app/cart.html")