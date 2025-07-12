from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator
# Create your views here.

def products(requst):
    all_products=Product.objects.all()
    page_number=requst.GET.get("page")
    paginator=Paginator(all_products,9)
    ithems_list=paginator.get_page(page_number)
    return render(requst,'products_app/products.html',context={'products':ithems_list})


def product(requst,slug):
    prod=Product.objects.get(slug=slug)
    return render(requst,'products_app/product.html',context={'product':prod})