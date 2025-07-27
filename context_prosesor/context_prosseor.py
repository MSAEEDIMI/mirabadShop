from home_app.models import SiteInfo


def site_info(request):
    siteInfo=SiteInfo.objects.last()
    title=siteInfo.title.split(" ") # type: ignore
    return {"siteInfo":siteInfo,"title":title}