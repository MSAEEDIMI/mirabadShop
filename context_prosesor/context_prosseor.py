from home_app.models import SiteInfo
from cart_app.cart import Cart


def site_info(request):
    siteInfo=SiteInfo.objects.last()
    title=siteInfo.title.split(" ") # type: ignore
    cart=Cart(request)
    return {"siteInfo":siteInfo,"title":title,'cart':cart}