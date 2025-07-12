from home_app.models import SiteInfo


def site_info(request):
    siteInfo=SiteInfo.objects.last()
    return {"siteInfo":siteInfo}