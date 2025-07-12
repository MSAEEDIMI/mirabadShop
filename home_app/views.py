from django.shortcuts import render
from .models import Banner
from products_app.models import Product , Category
from django.db.models import Q
from django.core.paginator import Paginator


# Create your views here.
def home_app(requst):
    # baners and slider
    main_banner = Banner.objects.filter(position='main').order_by('order')
    sidebar_banners = Banner.objects.filter(position='sidebar').order_by('order')[:3]
    footer_banners = Banner.objects.filter(position='footer').order_by('order')[:2]
    
    categorys=Category.objects.all()
    all_products =Product.objects.all()
    special_sale=Product.objects.filter(discount__gte=30).order_by('-discount',)    
    context={
        # baners and slider
        'main_banner': main_banner,
        'sidebar_banners': sidebar_banners,
        'footer_banners': footer_banners,
        
        # product 
        'categorys':categorys,
        'products':all_products,
        'special_sale':special_sale
    }
    return render(requst,"home_app/index.html",context=context)

def serach(requst):
    serarch_word=requst.GET.get("search_word")
    all_products =Product.objects.filter(name__icontains=serarch_word)
    page_number=requst.GET.get("page")
    paginator=Paginator(all_products,6)
    ithems_list=paginator.get_page(page_number)
    return render(requst,'products_app/products.html',context={'products':ithems_list})