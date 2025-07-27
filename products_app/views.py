from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator
from django.views.generic.detail import DetailView


def products(requst):
    all_products=Product.objects.all()
    page_number=requst.GET.get("page")
    paginator=Paginator(all_products,5)
    ithems_list=paginator.get_page(page_number)
    return render(requst,'products_app/products.html',context={'products':ithems_list})


class ProductsDetailView(DetailView):
    model=Product
    template_name="products_app/product.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all()
        return context
    